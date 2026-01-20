import json
import logging
import os
import tempfile
from io import BytesIO

import requests
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
ELEVENLABS_API_KEY = "your api key"
TELEGRAM_BOT_TOKEN = "your bot token"

# Voice mappings
VOICES = {
    "yui": "fUjY9K2nAIwlALOwSiwc",
    "awaro": "EbuvaInXUGWtpYRUnKLQ",
    "sakuya": "8kgj5469z1URcH4MB2G4",
}

# Admin storage
ADMINS_FILE = "admins.json"

# Default admin IDs (main admins)
DEFAULT_ADMIN_IDS = [5770792085]


class AdminManager:
    def __init__(self, admins_file):
        self.admins_file = admins_file
        self.load_admins()

    def load_admins(self):
        """Load admins from JSON file"""
        try:
            if os.path.exists(self.admins_file):
                with open(self.admins_file, "r") as f:
                    data = json.load(f)
                    self.main_admins = data.get("main_admins", DEFAULT_ADMIN_IDS)
                    self.sub_admins = data.get("sub_admins", [])
            else:
                self.main_admins = DEFAULT_ADMIN_IDS.copy()
                self.sub_admins = []
                self.save_admins()
        except Exception as e:
            logger.error(f"Error loading admins: {e}")
            self.main_admins = DEFAULT_ADMIN_IDS.copy()
            self.sub_admins = []

    def save_admins(self):
        """Save admins to JSON file"""
        try:
            data = {"main_admins": self.main_admins, "sub_admins": self.sub_admins}
            with open(self.admins_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving admins: {e}")

    def is_main_admin(self, user_id):
        """Check if user is main admin"""
        return user_id in self.main_admins

    def is_sub_admin(self, user_id):
        """Check if user is sub admin"""
        return user_id in self.sub_admins

    def is_admin(self, user_id):
        """Check if user is any type of admin"""
        return self.is_main_admin(user_id) or self.is_sub_admin(user_id)

    def add_sub_admin(self, user_id):
        """Add user as sub admin"""
        if user_id not in self.sub_admins and not self.is_main_admin(user_id):
            self.sub_admins.append(user_id)
            self.save_admins()
            return True
        return False

    def remove_sub_admin(self, user_id):
        """Remove user from sub admins"""
        if user_id in self.sub_admins:
            self.sub_admins.remove(user_id)
            self.save_admins()
            return True
        return False

    def get_all_admins(self):
        """Get all admins (main + sub)"""
        return {"main_admins": self.main_admins, "sub_admins": self.sub_admins}


# Initialize admin manager
admin_manager = AdminManager(ADMINS_FILE)


class ElevenLabsTTS:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"

    def generate_audio(self, text, voice_id, model_id="eleven_multilingual_v2"):
        """Generate audio using ElevenLabs API v2 model"""
        url = f"{self.base_url}/text-to-speech/{voice_id}"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key,
        }

        data = {
            "text": text,
            "model_id": model_id,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
        }

        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            response.raise_for_status()
            return BytesIO(response.content)
        except requests.exceptions.RequestException as e:
            logger.error(f"ElevenLabs API error: {e}")
            return None


# Initialize TTS client
tts_client = ElevenLabsTTS(ELEVENLABS_API_KEY)


def is_admin(user_id):
    """Check if user is admin (main or sub)"""
    return admin_manager.is_admin(user_id)


def is_main_admin(user_id):
    """Check if user is main admin"""
    return admin_manager.is_main_admin(user_id)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the command /start is issued."""
    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text("❌ You are not authorized to use this bot.")
        return

    welcome_text = """
 Voice Note Bot

Available commands:
/vn [voice] [text] - Generate voice note

Available voices:
• yui - Female voice
• awaro - Male voice
• sakuya - Female voice

Example:
/vn yui Hello, how are you today?
    """
    await update.message.reply_text(welcome_text)


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin management command"""
    user_id = update.effective_user.id

    # Check if user is main admin
    if not is_main_admin(user_id):
        await update.message.reply_text("❌ Only main admins can use this command.")
        return

    # Check if replying to a message
    if update.message.reply_to_message:
        target_user_id = update.message.reply_to_message.from_user.id
        target_username = (
            update.message.reply_to_message.from_user.username
            or update.message.reply_to_message.from_user.first_name
        )

        if admin_manager.add_sub_admin(target_user_id):
            await update.message.reply_text(
                f"✅ User @{target_username} (ID: {target_user_id}) added as sub-admin!"
            )
        else:
            await update.message.reply_text(
                f"❌ User @{target_username} is already an admin or sub-admin!"
            )
        return

    # Check for specific commands
    if not context.args:
        await update.message.reply_text(
            "👮 Admin Management\n\n"
            "Usage:\n"
            "• Reply to a user's message with /admin to add them as sub-admin\n"
            "• /admin add [user_id] - Add user by ID\n"
            "• /admin remove [user_id] - Remove sub-admin\n"
            "• /admin list - List all admins\n"
            "• /admin status - Check your admin status"
        )
        return

    command = context.args[0].lower()

    if command == "add" and len(context.args) > 1:
        try:
            target_user_id = int(context.args[1])
            if admin_manager.add_sub_admin(target_user_id):
                await update.message.reply_text(
                    f"✅ User ID {target_user_id} added as sub-admin!"
                )
            else:
                await update.message.reply_text(
                    f"❌ User ID {target_user_id} is already an admin!"
                )
        except ValueError:
            await update.message.reply_text("❌ Invalid user ID!")

    elif command == "remove" and len(context.args) > 1:
        try:
            target_user_id = int(context.args[1])
            if admin_manager.remove_sub_admin(target_user_id):
                await update.message.reply_text(
                    f"✅ User ID {target_user_id} removed from sub-admins!"
                )
            else:
                await update.message.reply_text(
                    f"❌ User ID {target_user_id} is not a sub-admin!"
                )
        except ValueError:
            await update.message.reply_text("❌ Invalid user ID!")

    elif command == "list":
        admins = admin_manager.get_all_admins()

        main_admins_text = "\n".join(
            [f"• {admin_id}" for admin_id in admins["main_admins"]]
        )
        sub_admins_text = (
            "\n".join([f"• {admin_id}" for admin_id in admins["sub_admins"]])
            if admins["sub_admins"]
            else "No sub-admins"
        )

        admin_list = (
            f"👑 Main Admins:\n{main_admins_text}\n\n👥 Sub Admins:\n{sub_admins_text}"
        )
        await update.message.reply_text(admin_list)

    elif command == "status":
        if is_main_admin(user_id):
            status = "👑 Main Admin"
        elif is_admin(user_id):
            status = "👥 Sub Admin"
        else:
            status = "❌ Not Admin"

        await update.message.reply_text(f"Your status: {status}\nUser ID: {user_id}")

    else:
        await update.message.reply_text("❌ Invalid admin command!")


async def voice_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate and send voice note"""
    user_id = update.effective_user.id

    # Check if user is admin (main or sub)
    if not is_admin(user_id):
        await update.message.reply_text("❌ You are not authorized to use this bot.")
        return

    # Check if arguments are provided
    if not context.args:
        await update.message.reply_text(
            "Usage: /vn [voice] [text]\n\n"
            "Available voices: yui, awaro, sakuya\n"
            "Example: /vn yui Hello world!"
        )
        return

    # Extract voice and text
    try:
        voice_name = context.args[0].lower()
        text = " ".join(context.args[1:])
    except IndexError:
        await update.message.reply_text("❌ Please provide both voice and text.")
        return

    # Validate voice
    if voice_name not in VOICES:
        available_voices = ", ".join(VOICES.keys())
        await update.message.reply_text(
            f"❌ Invalid voice. Available voices: {available_voices}"
        )
        return

    # Validate text
    if not text.strip():
        await update.message.reply_text("❌ Please provide text to convert.")
        return

    if len(text) > 1000:
        await update.message.reply_text("❌ Text too long. Maximum 1000 characters.")
        return

    # Send processing message
    processing_msg = await update.message.reply_text("🔄 Generating voice note...")

    # Generate audio
    voice_id = VOICES[voice_name]
    audio_data = tts_client.generate_audio(text, voice_id)

    if audio_data is None:
        await processing_msg.edit_text("❌ Error generating audio. Please try again.")
        return

    # Send voice note
    try:
        audio_data.seek(0)
        await update.message.reply_voice(
            voice=audio_data,
            filename=f"{voice_name}_voice_note.mp3",
            caption=f" Voice: {voice_name}\n Text: {text[:100]}{'...' if len(text) > 100 else ''}",
        )
        await processing_msg.delete()

    except Exception as e:
        logger.error(f"Error sending voice note: {e}")
        await processing_msg.edit_text("❌ Error sending voice note. Please try again.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message"""
    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text("❌ You are not authorized to use this bot.")
        return

    help_text = """
Voice Note Bot Help

Commands:
/start - Start the bot
/help - Show this help message
/vn [voice] [text] - Generate voice note
/admin - Admin management (main admins only)

Available Voices:
• yui - Female Japanese-inspired voice
• awaro - Male voice
• sakuya - Female voice

Examples:
/vn yui Hello, how are you?
/vn awaro This is a test message
/vn sakuya Welcome to our service!

Note: Only admins can use this bot.
    """
    await update.message.reply_text(help_text)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Exception while handling an update: {context.error}")


def main():
    """Start the bot"""
    # Create Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("vn", voice_note))
    application.add_handler(CommandHandler("admin", admin_command))

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the Bot
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
