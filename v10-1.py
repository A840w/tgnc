#!/usr/bin/env python3

# Telegram GC Name Changer - Multi-Bot Turbo Mode
# Python version with bot token saving feature

import urllib.parse
import urllib.request
import random
import time
import threading
import os
import sys
import json

# Configuration
SUFFIXES = ["fun nc", "super fast nc", "nc bc", "turbo nc", "speed nc", "rapid nc"]
EMOJIS = ["🖐🏿", "✋🏿", "👌🏿", "🤌🏿", "👍🏿", "👎🏿", "🤙🏿", "🤘🏿", "🫴🏿", "🫳🏿", "✍🏿", "👏🏿", "👐🏿", "🫶🏿", "🙌🏿", "🤲🏿", "🙏🏿", "💪🏿", "🤏🏿", "👆🏿", "☝🏿"]

# Add admin user IDs here (numeric Telegram user IDs)
ADMIN_USER_IDS = ["123456789", "987654321"]  # Replace with actual admin user IDs

# File configuration
TOKENS_FILE = "bot_tokens.json"

# Colors for output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

# Global variables
BOT_TOKENS = []
ACTIVE_THREADS = []

def save_tokens_to_file():
    """Save bot tokens to file"""
    try:
        with open(TOKENS_FILE, 'w') as f:
            json.dump(BOT_TOKENS, f)
        print(f"{Colors.GREEN}Bot tokens saved to {TOKENS_FILE}{Colors.NC}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error saving tokens: {e}{Colors.NC}")
        return False

def load_tokens_from_file():
    """Load bot tokens from file"""
    global BOT_TOKENS
    try:
        if os.path.exists(TOKENS_FILE):
            with open(TOKENS_FILE, 'r') as f:
                loaded_tokens = json.load(f)
                if isinstance(loaded_tokens, list):
                    BOT_TOKENS = loaded_tokens
                    print(f"{Colors.GREEN}Loaded {len(BOT_TOKENS)} bot tokens from {TOKENS_FILE}{Colors.NC}")
                    return True
        return False
    except Exception as e:
        print(f"{Colors.RED}Error loading tokens: {e}{Colors.NC}")
        return False

def clear_saved_tokens():
    """Clear all saved bot tokens"""
    global BOT_TOKENS
    try:
        if os.path.exists(TOKENS_FILE):
            os.remove(TOKENS_FILE)
        BOT_TOKENS = []
        print(f"{Colors.GREEN}All saved bot tokens have been cleared{Colors.NC}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error clearing tokens: {e}{Colors.NC}")
        return False

def view_saved_tokens():
    """View all saved bot tokens"""
    if not BOT_TOKENS:
        print(f"{Colors.YELLOW}No bot tokens saved{Colors.NC}")
        return
    
    print(f"{Colors.CYAN}=== SAVED BOT TOKENS ==={Colors.NC}")
    for i, token in enumerate(BOT_TOKENS, 1):
        print(f"{i}. ...{token[-10:]}")
    print()

def remove_bot_token():
    """Remove specific bot token"""
    if not BOT_TOKENS:
        print(f"{Colors.YELLOW}No bot tokens to remove{Colors.NC}")
        return
    
    view_saved_tokens()
    try:
        choice = int(input(f"{Colors.YELLOW}Enter token number to remove (0 to cancel): {Colors.NC}"))
        if choice == 0:
            return
        if 1 <= choice <= len(BOT_TOKENS):
            removed_token = BOT_TOKENS.pop(choice - 1)
            save_tokens_to_file()
            print(f"{Colors.GREEN}Token ...{removed_token[-10:]} removed successfully{Colors.NC}")
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.NC}")
    except ValueError:
        print(f"{Colors.RED}Please enter a valid number{Colors.NC}")

def is_admin(user_id):
    """Check if user is admin"""
    return user_id in ADMIN_USER_IDS

def random_suffix():
    """Get random suffix"""
    return random.choice(SUFFIXES)

def random_emoji():
    """Get random emoji"""
    return random.choice(EMOJIS)

def random_name(prefix):
    """Generate random name"""
    return f"{prefix} {random_suffix()} {random_emoji()}"

def url_encode(text):
    """URL encode text"""
    return urllib.parse.quote(text)

def set_chat_title(bot_token, chat_id, title):
    """Set chat title via Telegram API"""
    try:
        encoded_title = url_encode(title)
        url = f"https://api.telegram.org/bot{bot_token}/setChatTitle"
        data = f"chat_id={chat_id}&title={encoded_title}".encode('utf-8')
        
        request = urllib.request.Request(url, data=data, method='POST')
        urllib.request.urlopen(request, timeout=2)
    except Exception:
        pass  # Silently fail for speed

def send_message(bot_token, chat_id, text):
    """Send message via bot"""
    try:
        encoded_text = url_encode(text)
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = f"chat_id={chat_id}&text={encoded_text}".encode('utf-8')
        
        request = urllib.request.Request(url, data=data, method='POST')
        urllib.request.urlopen(request, timeout=2)
    except Exception:
        pass  # Silently fail

def turbo_spam(bot_token, chat_id, prefix, thread_id):
    """Ultra fast spam function for individual bot"""
    bot_suffix = bot_token[-4:]
    print(f"{Colors.GREEN}Thread {thread_id} started for bot ...{bot_suffix}{Colors.NC}")
    
    counter = 0
    while True:
        new_name = random_name(prefix)
        set_chat_title(bot_token, chat_id, new_name)
        
        counter += 1
        if counter % 50 == 0:
            print(f"{Colors.CYAN}Thread {thread_id} (...{bot_suffix}): {counter} name changes{Colors.NC}")
        
        # Ultra fast - minimal sleep for maximum speed
        time.sleep(0.02)

def start_turbo_nc(chat_id, prefix):
    """Start turbo name changing with all bots"""
    print(f"{Colors.PURPLE}🚀 STARTING TURBO MODE 🚀{Colors.NC}")
    print(f"{Colors.YELLOW}Chat ID: {chat_id}{Colors.NC}")
    print(f"{Colors.YELLOW}Prefix: {prefix}{Colors.NC}")
    print(f"{Colors.YELLOW}Active Bots: {len(BOT_TOKENS)}{Colors.NC}")
    print(f"{Colors.GREEN}Press Ctrl+C to stop turbo mode{Colors.NC}")
    
    # Clear previous active threads
    global ACTIVE_THREADS
    ACTIVE_THREADS = []
    
    # Start each bot in its own thread
    thread_count = 0
    for bot_token in BOT_TOKENS:
        thread_count += 1
        thread = threading.Thread(target=turbo_spam, args=(bot_token, chat_id, prefix, thread_count))
        thread.daemon = True
        thread.start()
        ACTIVE_THREADS.append(thread)
        print(f"{Colors.GREEN}Started thread {thread_count} for bot{Colors.NC}")
        
        # Small delay between thread starts to avoid rate limiting
        time.sleep(0.1)
    
    print(f"{Colors.CYAN}All {thread_count} threads started! Running at maximum speed...{Colors.NC}")
    
    # Wait for all threads (though they run indefinitely)
    try:
        for thread in ACTIVE_THREADS:
            thread.join()
    except KeyboardInterrupt:
        stop_turbo_nc()

def stop_turbo_nc():
    """Stop all active threads"""
    print(f"{Colors.YELLOW}Stopping all turbo threads...{Colors.NC}")
    # Since we're using daemon threads, they'll exit when main thread exits
    ACTIVE_THREADS.clear()
    print(f"{Colors.GREEN}All threads stopped!{Colors.NC}")

def add_bot_token():
    """Add bot token interactively"""
    print(f"{Colors.YELLOW}Enter bot token (or 'q' to finish):{Colors.NC}")
    bot_token = input("Bot Token: ").strip()
    
    if bot_token.lower() == 'q':
        return False
    
    if bot_token:
        BOT_TOKENS.append(bot_token)
        save_tokens_to_file()
        print(f"{Colors.GREEN}Bot token added! Total bots: {len(BOT_TOKENS)}{Colors.NC}")
        return True
    else:
        print(f"{Colors.RED}Invalid bot token!{Colors.NC}")
        return False

def show_bot_status():
    """Show bot status"""
    print(f"{Colors.CYAN}=== BOT STATUS ==={Colors.NC}")
    print(f"Total Bots: {len(BOT_TOKENS)}")
    print(f"Active Threads: {len(ACTIVE_THREADS)}")
    print()
    view_saved_tokens()

def test_bot_token(bot_token):
    """Test bot token"""
    print(f"{Colors.YELLOW}Testing bot token...{Colors.NC}")
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        response = urllib.request.urlopen(url, timeout=5)
        response_data = response.read().decode('utf-8')
        
        if '"ok":true' in response_data:
            print(f"{Colors.GREEN}✓ Bot token is valid!{Colors.NC}")
            # Extract bot username
            if '"username":"' in response_data:
                username_start = response_data.find('"username":"') + 12
                username_end = response_data.find('"', username_start)
                bot_name = response_data[username_start:username_end]
                print(f"{Colors.GREEN}Bot Username: @{bot_name}{Colors.NC}")
            return True
    except Exception:
        pass
    
    print(f"{Colors.RED}✗ Invalid bot token!{Colors.NC}")
    return False

def test_all_bots():
    """Test all saved bot tokens"""
    if not BOT_TOKENS:
        print(f"{Colors.YELLOW}No bots to test{Colors.NC}")
        return
    
    print(f"{Colors.YELLOW}Testing all bot tokens...{Colors.NC}")
    valid_bots = []
    invalid_bots = []
    
    for bot_token in BOT_TOKENS:
        if test_bot_token(bot_token):
            valid_bots.append(bot_token)
        else:
            invalid_bots.append(bot_token)
    
    # Update with only valid bots
    if invalid_bots:
        BOT_TOKENS.clear()
        BOT_TOKENS.extend(valid_bots)
        save_tokens_to_file()
        print(f"{Colors.GREEN}Valid bots: {len(valid_bots)}, Invalid bots removed: {len(invalid_bots)}{Colors.NC}")
    else:
        print(f"{Colors.GREEN}All {len(valid_bots)} bots are valid!{Colors.NC}")

def interactive_setup():
    """Interactive setup function"""
    print(f"{Colors.PURPLE}================================={Colors.NC}")
    print(f"{Colors.PURPLE}   TELEGRAM TURBO NC SETUP       {Colors.NC}")
    print(f"{Colors.PURPLE}================================={Colors.NC}")
    print()
    
    # Show current saved tokens
    if BOT_TOKENS:
        print(f"{Colors.GREEN}Found {len(BOT_TOKENS)} saved bot tokens{Colors.NC}")
        view_saved_tokens()
        
        use_saved = input(f"{Colors.YELLOW}Use saved tokens? (y/n): {Colors.NC}").strip().lower()
        if use_saved != 'y':
            # Add new bot tokens
            print(f"{Colors.YELLOW}Adding new bot tokens...{Colors.NC}")
            while True:
                if not add_bot_token():
                    break
    else:
        print(f"{Colors.YELLOW}No saved tokens found. Adding new bot tokens...{Colors.NC}")
        while True:
            if not add_bot_token():
                break
    
    if not BOT_TOKENS:
        print(f"{Colors.RED}No bots added! Exiting.{Colors.NC}")
        sys.exit(1)
    
    # Test all bots
    test_all_bots()
    
    if not BOT_TOKENS:
        print(f"{Colors.RED}No valid bots! Exiting.{Colors.NC}")
        sys.exit(1)
    
    # Get chat ID and prefix
    print()
    print(f"{Colors.YELLOW}Enter Chat ID (group/channel ID):{Colors.NC}")
    chat_id = input("Chat ID: ").strip()
    
    print(f"{Colors.YELLOW}Enter name prefix:{Colors.NC}")
    prefix = input("Prefix: ").strip()
    
    if not chat_id or not prefix:
        print(f"{Colors.RED}Chat ID and Prefix are required!{Colors.NC}")
        sys.exit(1)
    
    # Show summary and start
    print()
    print(f"{Colors.CYAN}=== SETUP SUMMARY ==={Colors.NC}")
    print(f"Bots: {len(BOT_TOKENS)}")
    print(f"Chat ID: {chat_id}")
    print(f"Prefix: {prefix}")
    print()
    
    print(f"{Colors.YELLOW}Starting in 3 seconds...{Colors.NC}")
    time.sleep(3)
    
    # Start turbo mode
    start_turbo_nc(chat_id, prefix)

def get_updates(bot_token, offset):
    """Get updates from Telegram API"""
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getUpdates?offset={offset}&timeout=10"
        response = urllib.request.urlopen(url, timeout=15)
        return response.read().decode('utf-8')
    except Exception:
        return ""

def extract_updates(response):
    """Extract updates from response"""
    updates = []
    response_lines = response.split('\n')
    
    i = 0
    while i < len(response_lines):
        line = response_lines[i]
        if '"update_id":' in line:
            update = {}
            # Extract update_id
            if '"update_id":' in line:
                update_id = line.split(':')[1].strip().rstrip(',')
                update['update_id'] = update_id
            
            # Look for chat info
            j = i
            while j < min(i + 10, len(response_lines)):
                chat_line = response_lines[j]
                if '"chat":{"id":' in chat_line:
                    chat_id = chat_line.split(':')[-1].strip().rstrip(',')
                    update['chat_id'] = chat_id
                elif '"text":"' in chat_line:
                    text_start = chat_line.find('"text":"') + 8
                    text_end = chat_line.find('"', text_start)
                    update['text'] = chat_line[text_start:text_end]
                elif '"from":{"id":' in chat_line:
                    user_id = chat_line.split(':')[-1].strip().rstrip(',')
                    update['user_id'] = user_id
                j += 1
            
            if 'update_id' in update and 'chat_id' in update and 'text' in update:
                updates.append(update)
        i += 1
    
    return updates

def handle_rename_command(bot_token, chat_id, message_text, user_id):
    """Handle rename command"""
    if not is_admin(user_id):
        send_message(bot_token, chat_id, "bot use krne ki aukat bana phele 😏")
        return
    
    parts = message_text.split(' ', 1)
    if len(parts) < 2:
        send_message(bot_token, chat_id, "Usage: /renam <prefix>")
        return
    
    prefix = parts[1]
    send_message(bot_token, chat_id, f"🚀 TURBO MODE ACTIVATED! Prefix: {prefix}")
    
    # Start turbo mode in a separate thread
    thread = threading.Thread(target=start_turbo_nc, args=(chat_id, prefix))
    thread.daemon = True
    thread.start()

def poll_messages(bot_token):
    """Handle polling for messages (for command mode)"""
    last_update_id = 0
    
    print(f"{Colors.GREEN}Command mode started for control bot...{Colors.NC}")
    
    while True:
        response = get_updates(bot_token, last_update_id + 1)
        updates = extract_updates(response)
        
        for update in updates:
            last_update_id = int(update['update_id'])
            chat_id = update.get('chat_id', '')
            message_text = update.get('text', '')
            user_id = update.get('user_id', '')
            
            if message_text.startswith('/renam'):
                handle_rename_command(bot_token, chat_id, message_text, user_id)
            elif message_text.startswith('/stop'):
                stop_turbo_nc()
                send_message(bot_token, chat_id, "Turbo NC stopped!")
        
        time.sleep(1)

def manage_tokens_menu():
    """Menu for managing bot tokens"""
    while True:
        print(f"{Colors.CYAN}=== BOT TOKEN MANAGEMENT ==={Colors.NC}")
        print(f"1. {Colors.GREEN}View Saved Tokens{Colors.NC}")
        print(f"2. {Colors.BLUE}Add New Token{Colors.NC}")
        print(f"3. {Colors.YELLOW}Remove Token{Colors.NC}")
        print(f"4. {Colors.RED}Clear All Tokens{Colors.NC}")
        print(f"5. {Colors.PURPLE}Test All Tokens{Colors.NC}")
        print(f"6. {Colors.CYAN}Back to Main Menu{Colors.NC}")
        print()
        
        choice = input(f"{Colors.YELLOW}Select option (1-6): {Colors.NC}").strip()
        
        if choice == '1':
            view_saved_tokens()
        elif choice == '2':
            add_bot_token()
        elif choice == '3':
            remove_bot_token()
        elif choice == '4':
            confirm = input(f"{Colors.RED}Are you sure you want to clear ALL tokens? (y/n): {Colors.NC}").strip().lower()
            if confirm == 'y':
                clear_saved_tokens()
        elif choice == '5':
            test_all_bots()
        elif choice == '6':
            break
        else:
            print(f"{Colors.RED}Invalid option!{Colors.NC}")
        
        print()

def main_menu():
    """Main menu"""
    # Load saved tokens on startup
    load_tokens_from_file()
    
    while True:
        print(f"{Colors.PURPLE}================================={Colors.NC}")
        print(f"{Colors.PURPLE}    TELEGRAM TURBO NC MENU       {Colors.NC}")
        print(f"{Colors.PURPLE}================================={Colors.NC}")
        print()
        print(f"1. {Colors.GREEN}Interactive Turbo Mode{Colors.NC} (Recommended)")
        print(f"2. {Colors.YELLOW}Command Mode{Colors.NC} (Use /renam in groups)")
        print(f"3. {Colors.BLUE}Manage Bot Tokens{Colors.NC}")
        print(f"4. {Colors.CYAN}Show Bot Status{Colors.NC}")
        print(f"5. {Colors.RED}Stop All Threads{Colors.NC}")
        print(f"6. {Colors.PURPLE}Exit{Colors.NC}")
        print()
        
        try:
            choice = input("Select option (1-6): ").strip()
            
            if choice == '1':
                interactive_setup()
            elif choice == '2':
                if not BOT_TOKENS:
                    print(f"{Colors.RED}No bots added! Use option 3 first.{Colors.NC}")
                    time.sleep(2)
                else:
                    print(f"{Colors.YELLOW}Starting command mode...{Colors.NC}")
                    poll_messages(BOT_TOKENS[0])
            elif choice == '3':
                manage_tokens_menu()
            elif choice == '4':
                show_bot_status()
            elif choice == '5':
                stop_turbo_nc()
            elif choice == '6':
                stop_turbo_nc()
                print(f"{Colors.GREEN}Goodbye!{Colors.NC}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}Invalid option!{Colors.NC}")
        except KeyboardInterrupt:
            stop_turbo_nc()
            print(f"\n{Colors.GREEN}Goodbye!{Colors.NC}")
            sys.exit(0)

def install_dependencies():
    """Check if running in appropriate environment"""
    # Python standard library should have all needed modules
    # This is just a placeholder for compatibility
    pass

if __name__ == "__main__":
    try:
        install_dependencies()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Shutting down...{Colors.NC}")
        stop_turbo_nc()
        sys.exit(0)