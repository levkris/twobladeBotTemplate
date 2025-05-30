# 🧠 twobladeBotTemplate

This is a template to make a bot for [twoblade](https://twoblade.com) using Selenium.

## 🐍 Requirements

- **Python 3.13.0** (or later — tested on 3.13.0)
- **pip** (Python's package installer)

## 📦 Installing Dependencies

After installing Python and pip, run:

```bash
pip install -r requirements.txt
```

---

## 🛠️ How to Install Python

### 💻 Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/windows/).
2. Download the latest version for Windows (tested on Python 3.13.0).
3. Run the installer:
   - ✅ Check **"Add Python to PATH"**
   - ▶️ Click **"Install Now"**
4. Done! You can verify with:
   ```powershell
   python --version
   ```

### 🍏 macOS

1. Use [Homebrew](https://brew.sh/) (recommended):
   ```bash
   brew install python
   ```
2. Or download manually from [python.org/downloads](https://www.python.org/downloads/macos/)

3. Check if it worked:
   ```bash
   python3 --version
   ```

### 🐧 Linux (Debian/Ubuntu)

1. Open a terminal and run:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
2. Check:
   ```bash
   python3 --version
   pip3 --version
   ```

> For Arch, Fedora, etc., use your package manager (`pacman`, `dnf`, etc.)

---

## 📁 Project Structure

```
twobladeBotTemplate/
├── template.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Configuration

Inside `template.py`, you’ll find a few variables you **must update** to suit your bot:

```python
REPLIED_FILE = "yourFile.json"         # Replace with your actual file name

botName = "Your Bot Name"              # Replace with your actual bot name
botUsername = "YourBotUsername"        # Replace with your actual bot username
botPassword = "YourBotPassword"        # Replace with your actual bot password

maxMessages = 10                       # Maximum number of messages to process
```

Make sure to configure these before running the bot!

---

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).
