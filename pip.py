import os
import sys
import subprocess
import time

# Color codes
C = "\033[1;91m"
S = "\033[1;91m"
N = "\033[1;94m"
V = "\033[1;94m"
reset = "\033[0m"
n = "\033[38;2;0;135;215m"
v = "\033[38;2;0;0;95m"
grey = "\033[38;2;200;200;200m"
green = "\033[1;92m"
yellow = "\033[1;93m"
bold = "\033[1m"

url = "https://t.me/baddieprotecter"


def clear_screen():
    """Clear screen (works in Termux/Linux/Windows)"""
    os.system('cls' if os.name == 'nt' else 'clear')


def install_packages():
    print(f"{grey}Installing required Python packages. Please wait...\n")
    print(f"{C} C{S} S{N} N{V} V{grey} {C} C{S} S{n} N{v} V\n")

    pkgs = [
        ("cfonts", "cfonts"),
        ("pyfiglet", "pyfiglet"),
        ("rich", "rich")
    ]

    for package, pip_name in pkgs:
        try:
            __import__(package)
            print(f"{green}[+] {package} is already installed.")
        except ImportError:
            print(f"{yellow}[➤] Installing {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
                print(f"{green}[+] {package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"{C}✖ Failed with sys.executable, retrying with pip...")
                try:
                    subprocess.check_call(["pip", "install", pip_name])
                    print(f"{green}[+] {package} installed successfully.")
                except subprocess.CalledProcessError as e2:
                    print(f"{C}✖ Could not install {package}. Error: {e2}")


def main():
    clear_screen()
    time.sleep(1)
    print(f"{C} C{S} S{N} N{V} V{grey} {C} b{S} a{n} n{v} e")
    print("-" * 60)
    print(f"{green}[+] All packages processed successfully.")
    print(f"{n}You can now run the script.")
    print(f"{n}If you face any issues, contact us at {url}")
    print(f"{n}Thank you for using my script.")
    print("-" * 60)
    print(reset)


if __name__ == "__main__":
    install_packages()
    main()
