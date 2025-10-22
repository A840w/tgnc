import os
import sys
import subprocess
import time
import platform

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

url = "https://t.me/+svrl2mWRUV1jNDc1"


def clear_screen():
    """Cross-platform screen clearing"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


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
                # Use sys.executable to ensure we're using the correct Python interpreter
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", pip_name
                ])
                print(f"{green}[+] {package} has been installed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"{C}✖ Failed to install {package}. Error: {e}")
                # Try alternative installation method
                try:
                    print(f"{yellow}[➤] Trying alternative installation method for {package}...")
                    subprocess.check_call(["pip", "install", pip_name])
                    print(f"{green}[+] {package} has been installed successfully.")
                except subprocess.CalledProcessError as e2:
                    print(f"{C}✖ Alternative installation also failed for {package}. Error: {e2}")
            except Exception as e:
                print(f"{C}✖ Unexpected error installing {package}: {e}")


def main():
    print(f"\n{C} C{S} S{N} N{V} V{grey} {C} C{S} S{n} N{v} V")
    clear_screen()
    time.sleep(2)
    print(f"{C} C{S} S{N} N{V} V{grey} {C} b{S} a{n} n{v} e")
    print("-" * 60)
    print(f"{green}[+] All packages have been processed successfully.")
    print(f"{n}You can now run the script.")
    print(f"{n}If you face any issues, please contact us at {url}")
    print(f"{n}Thank you for using my script.")
    print("-" * 60)
    print(reset)


if __name__ == "__main__":
    install_packages()
    main()