
import urllib.parse
import urllib.request
import random
import time
import threading
import os
import sys
import os
from pyfiglet import figlet_format
from cfonts import render


CG = {
    'RD': '\033[1;31m','gn': '\033[1;32m','ylo': '\033[1;33m','cya?': '\033[36m','bl': '\033[1;34m','rt': '\033[0m','gd': '\x1b[38;5;220m','BD': '\033[1m',
}
BGCG = {
    'BK'     : '\033[40m','RD'       : '\033[41m','gn'     : '\033[42m','ylo'    : '\033[43m','bl'      : '\033[44m','MG'   : '\033[45m','cya?'      : '\033[46m','white'     : '\033[47m'
}

BG256 = {
    'bright_MG' : '\033[48;5;201m',
    'bright_bl'    : '\033[48;5;117m',
    'bright_gn'   : '\033[48;5;82m',
    'bright_ylo'  : '\033[48;5;226m',
    'bright_cya?'    : '\033[48;5;87m',
    'bright_RD'     : '\033[48;5;196m',
    'gray'           : '\033[48;5;244m',
    'orange'         : '\033[48;5;208m',
    'purple'         : '\033[48;5;93m'
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")
def logo():
    clear()
    print(render("• CSNV •", colors=["red", "blue"]))
    print(CG['bl'] + "Telegram Automation"+CG['rt']+BG256['purple']+ " NC " + CG['rt'])
    print(CG['ylo'] + "Created by BANE." + CG['rt'])
    print(CG['RD'] + "Version: v9 " + CG['rt'])
    print(CG['gn']+CG['BD']+ "multi bot\033[0m  "+BG256["bright_RD"]+"gc killer" + CG['rt'])
    print(BGCG['MG'] + "NO BATCH PROCESSING" + CG['rt'])
   # print(render("• CSNV •", CG=["RD", "bl"]))
logo()

SUFFIXES = ["ki ma बोली XLR8/GIGA/SYLAS से चूदूंगी🥀😅🤪", "ki ma कितनी बार चूदी ? 😲😲🤔🤔🤪🥀", " KE कितने बाप ?🤔🤔", "ki मां xlr8 से तेज तेज चूदी😲😲🤪🤣🤣🫵🏻❤️‍🔥", "tmkc", "atmkbfj"]
EMOJIS = [
" ˖ 😀་༘࿐",
" ˖ 😎་༘࿐",
" ˖ 🥳་༘࿐",
" ˖ 🤩་༘࿐",
" ˖ 🫡་༘࿐",
" ˖ 🥶་༘࿐",
" ˖ 😈་༘࿐",
" ˖ 👻་༘࿐",
" ˖ 🤖་༘࿐",
" ˖ 🎃་༘࿐",
" ˖ 🐵་༘࿐",
" ˖ 🦁་༘࿐",
" ˖ 🐯་༘࿐",
" ˖ 🐶་༘࿐",
" ˖ 🐱་༘࿐",
" ˖ 🦊་༘࿐",
" ˖ 🐻་༘࿐",
" ˖ 🐼་༘࿐",
" ˖ 🐨་༘࿐",
" ˖ 🐸་༘࿐",
" ˖ 🐧་༘࿐",
" ˖ 🦉་༘࿐",
" ˖ 🦋་༘࿐",
" ˖ 🐝་༘࿐",
" ˖ 🐞་༘࿐",
" ˖ 🐢་༘࿐",
" ˖ 🐍་༘࿐",
" ˖ 🦖་༘࿐",
" ˖ 🐙་༘࿐",
" ˖ 🐬་༘࿐",
" ˖ 🐳་༘࿐",
" ˖ 🐊་༘࿐",
" ˖ 🌲་༘࿐",
" ˖ 🌴་༘࿐",
" ˖ 🌵་༘࿐",
" ˖ 🌺་༘࿐",
" ˖ 🌻་༘࿐",
" ˖ 🌼་༘࿐",
" ˖ 🪻་༘࿐",
" ˖ 🪷་༘࿐",
" ˖ 🌹་༘࿐",
" ˖ 🌸་༘࿐",
" ˖ 🌙་༘࿐",
" ˖ ⭐་༘࿐",
" ˖ 🌈་༘࿐",
" ˖ ☀️་༘࿐",
" ˖ 🌊་༘࿐",
" ˖ 🌍་༘࿐",
" ˖ 🪐་༘࿐",
" ˖ 🔥་༘࿐",
" ˖ ❄️་༘࿐",
" ˖ ⚡་༘࿐",
" ˖ ☁️་༘࿐",
" ˖ 🌪️་༘࿐",
" ˖ 🌋་༘࿐",
" ˖ 🪨་༘࿐",
" ˖ 🧊་༘࿐",
" ˖ 🍎་༘࿐",
" ˖ 🍌་༘࿐",
" ˖ 🍇་༘࿐",
" ˖ 🍉་༘࿐",
" ˖ 🍓་༘࿐",
" ˖ 🍒་༘࿐",
" ˖ 🍑་༘࿐",
" ˖ 🥭་༘࿐",
" ˖ 🍍་༘࿐",
" ˖ 🥥་༘࿐",
" ˖ 🥑་༘࿐",
" ˖ 🌽་༘࿐",
" ˖ 🥕་༘࿐",
" ˖ 🥔་༘࿐",
" ˖ 🥦་༘࿐",
" ˖ 🍔་༘࿐",
" ˖ 🍕་༘࿐",
" ˖ 🍟་༘࿐",
" ˖ 🌭་༘࿐",
" ˖ 🍿་༘࿐",
" ˖ 🍩་༘࿐",
" ˖ 🎂་༘࿐",
" ˖ 🍪་༘࿐",
" ˖ 🍫་༘࿐",
" ˖ 🍬་༘࿐",
" ˖ 🍭་༘࿐",
" ˖ ☕་༘࿐",
" ˖ 🥤་༘࿐",
" ˖ 🍹་༘࿐",
" ˖ 🍺་༘࿐",
" ˖ 🍷་༘࿐",
" ˖ 🥂་༘࿐",
" ˖ ⚽་༘࿐",
" ˖ 🏀་༘࿐",
" ˖ 🏈་༘࿐",
" ˖ 🎾་༘࿐",
" ˖ 🏐་༘࿐",
" ˖ 🎮་༘࿐",
" ˖ 🎲་༘࿐",
" ˖ ♟️་༘࿐",
" ˖ 🧩་༘࿐",
" ˖ 🎯་༘࿐",
" ˖ 🎤་༘࿐",
" ˖ 🎧་༘࿐",
" ˖ 🎸་༘࿐",
" ˖ 🎹་༘࿐",
" ˖ 🥁་༘࿐",
" ˖ 🎷་༘࿐",
" ˖ 🎺་༘࿐",
" ˖ 🪗་༘࿐",
" ˖ 🏹་༘࿐",
" ˖ ⚔️་༘࿐",
" ˖ 🛡️་༘࿐",
" ˖ 🚗་༘࿐",
" ˖ 🏍️་༘࿐",
" ˖ 🚲་༘࿐",
" ˖ 🚂་༘࿐",
" ˖ 🛸་༘࿐",
" ˖ 🚀་༘࿐",
" ˖ ✈️་༘࿐",
" ˖ 🚁་༘࿐",
" ˖ 🚢་༘࿐",
" ˖ 🛶་༘࿐",
" ˖ ⚓་༘࿐",
" ˖ 🏖️་༘࿐",
" ˖ 🏔️་༘࿐",
" ˖ 🗼་༘࿐",
" ˖ 🗽་༘࿐",
" ˖ 🕌་༘࿐",
" ˖ ⛩️་༘࿐",
" ˖ 🏰་༘࿐",
" ˖ 🏯་༘࿐",
" ˖ 🏟️་༘࿐",
" ˖ 🛕་༘࿐",
" ˖ 🏝️་༘࿐",
" ˖ 🏜️་༘࿐"
]


ADMIN_USER_IDS = ["5770792085", "5538689569","5213627428",]  # Replace with actual admin user IDs


class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  


BOT_TOKENS = []
ACTIVE_THREADS = []

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
        pass 

def send_message(bot_token, chat_id, text):
    """Send message via bot"""
    try:
        encoded_text = url_encode(text)
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = f"chat_id={chat_id}&text={encoded_text}".encode('utf-8')
        
        request = urllib.request.Request(url, data=data, method='POST')
        urllib.request.urlopen(request, timeout=2)
    except Exception:
        pass 

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
        

        time.sleep(0.02)

def start_turbo_nc(chat_id, prefix):
    """Start name changing with all bots"""
    print(f"{Colors.PURPLE}MULTI BOT{Colors.NC}")
    print(f"{Colors.YELLOW}Chat ID: {chat_id}{Colors.NC}")
    print(f"{Colors.YELLOW}Prefix: {prefix}{Colors.NC}")
    print(f"{Colors.YELLOW}Active Bots: {len(BOT_TOKENS)}{Colors.NC}")
    print(f"{Colors.GREEN}Press Ctrl+C to stop {Colors.NC}")
    
  
    global ACTIVE_THREADS
    ACTIVE_THREADS = []
    
   
    thread_count = 0
    for bot_token in BOT_TOKENS:
        thread_count += 1
        thread = threading.Thread(target=turbo_spam, args=(bot_token, chat_id, prefix, thread_count))
        thread.daemon = True
        thread.start()
        ACTIVE_THREADS.append(thread)
        print(f"{Colors.GREEN}Started thread {thread_count} for bot{Colors.NC}")
        

        time.sleep(0.1)
    
    print(f"{Colors.CYAN}All {thread_count} threads started Running at maximum speed...{Colors.NC}")
    

    try:
        for thread in ACTIVE_THREADS:
            thread.join()
    except KeyboardInterrupt:
        stop_turbo_nc()

def stop_turbo_nc():
    """Stop all active threads"""
    print(f"{Colors.YELLOW}Stopping all turbo threads...{Colors.NC}")

    ACTIVE_THREADS.clear()
    print(f"{Colors.GREEN}All threads stopped{Colors.NC}")

def add_bot_token():
    """Add bot token interactively"""
    print(f"{Colors.YELLOW}Enter bot token (or 'q' to finish):{Colors.NC}")
    bot_token = input("Bot Token: ").strip()
    
    if bot_token.lower() == 'q':
        return False
    
    if bot_token:
        BOT_TOKENS.append(bot_token)
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
    print(f"{Colors.YELLOW}Bot Tokens:{Colors.NC}")
    for i, token in enumerate(BOT_TOKENS, 1):
        print(f"{i}. ...{token[-10:]}")
    print()

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

def interactive_setup():
    """Interactive setup function"""
    print(f"{Colors.PURPLE}================================={Colors.NC}")
    print(f"{Colors.PURPLE}   TELEGRAM NC SETUP       {Colors.NC}")
    print(f"{Colors.PURPLE}================================={Colors.NC}")
    print()
    
 
    while True:
        if not add_bot_token():
            break
    
    if not BOT_TOKENS:
        print(f"{Colors.RED}No bots added! Exiting.{Colors.NC}")
        sys.exit(1)
   
    print(f"{Colors.YELLOW}Testing bot tokens...{Colors.NC}")
    valid_bots = []
    for bot_token in BOT_TOKENS:
        if test_bot_token(bot_token):
            valid_bots.append(bot_token)
    
    BOT_TOKENS.clear()
    BOT_TOKENS.extend(valid_bots)
    print(f"{Colors.GREEN}Valid bots: {len(BOT_TOKENS)}{Colors.NC}")
    
    if not BOT_TOKENS:
        print(f"{Colors.RED}No valid bots! Exiting.{Colors.NC}")
        sys.exit(1)
    

    print()
    print(f"{Colors.YELLOW}Enter Chat ID (group/channel ID):{Colors.NC}")
    chat_id = input("Chat ID: ").strip()
    
    print(f"{Colors.YELLOW}Enter name prefix:{Colors.NC}")
    prefix = input("Prefix: ").strip()
    
    if not chat_id or not prefix:
        print(f"{Colors.RED}Chat ID and Prefix are required!{Colors.NC}")
        sys.exit(1)
    

    print()
    print(f"{Colors.CYAN}=== SETUP SUMMARY ==={Colors.NC}")
    print(f"Bots: {len(BOT_TOKENS)}")
    print(f"Chat ID: {chat_id}")
    print(f"Prefix: {prefix}")
    print()
    
    print(f"{Colors.YELLOW}Starting in 3 seconds...{Colors.NC}")
    time.sleep(3)
    

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

def main_menu():
    """Main menu"""
    print(f"{Colors.PURPLE}================================={Colors.NC}")
    print(f"{Colors.PURPLE}    TELEGRAM  NC MENU       {Colors.NC}")
    print(f"{Colors.PURPLE}================================={Colors.NC}")
    print()
    print(f"1. {Colors.GREEN}Interactive gt flow{Colors.NC} (Recommended)")
    print(f"2. {Colors.YELLOW}Command Mode{Colors.NC} (Use /renam in groups)")
    print(f"3. {Colors.BLUE}Add More Bots{Colors.NC}")
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
                print(f"{Colors.RED}No bots added Use option 1 first.{Colors.NC}")
                time.sleep(2)
                main_menu()
            else:
                print(f"{Colors.YELLOW}Starting command mode...{Colors.NC}")
                poll_messages(BOT_TOKENS[0])
        elif choice == '3':
            add_bot_token()
            main_menu()
        elif choice == '4':
            show_bot_status()
            main_menu()
        elif choice == '5':
            stop_turbo_nc()
            main_menu()
        elif choice == '6':
            stop_turbo_nc()
            print(f"{Colors.GREEN}acha bc{Colors.NC}")
            sys.exit(0)
        else:
            print(f"{Colors.RED}invald action{Colors.NC}")
            main_menu()
    except KeyboardInterrupt:
        stop_turbo_nc()
        print(f"\n{Colors.GREEN}acha bc{Colors.NC}")
        sys.exit(0)

def install_dependencies():
    """Check if running in appropriate environment"""

    pass

if __name__ == "__main__":
    try:
        install_dependencies()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Shutting down...{Colors.NC}")
        stop_turbo_nc()
        sys.exit(0)