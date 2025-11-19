# 🚀 Telegram Bot Toolkit

This repository contains two powerful Python scripts designed for Telegram automation and group management.  
It works seamlessly across **Mobile Termux**, **Pydroid**, **Linux**, and **Windows**.

---

## 📂 Project Files

- **`pip.py`** → Dependency installer (must be run first)
- **`v10.py`** → Fast group chat changer bot (terminal-based)
- **`allrounder.py`** → Multi-purpose bot with commands:
  - `/spam` → Send repeated messages quickly
  - `/gcnc` → Group chat name changer
  - `/slide` → Slide-style text effects

---

## ⚙️ Installation

Before running any bot script, make sure to install the required packages using `pip.py`.

### Termux (Android)
```bash
pkg install python -y
pkg install git -y
git clone <https://github.com/A840w/tgnc>
cd <tgnc>
python pip.py
python v10.py or tgnc.py