# ⚡ TELEFLOW v2.0: NETRUNNER EDITION

> **STATUS:** [UNSTABLE]
> **ACCESS:** [ROOT_GRANTED]
> **PROTOCOL:** [SECURE_UPLINK]

**Teleflow** is a premium, high-performance Telegram video downloader with a **cinematic "Hacker" terminal interface**. Designed for those who want their tools to look as powerful as they are.

---

## 🟢 SYSTEM CAPABILITIES

* **🕵️‍♂️ Netrunner UI:** A fully immersive, resize-proof terminal interface with glitch effects, binary rain, and hacker jargon.
* **🚀 High-Speed Exfiltration:** Multi-threaded download engine powered by `Telethon`.
* **📂 Smart Indexing:** Zero-padded numeric indexing (`[01]`, `[02]`) for rapid target selection—no more typing random hex codes.
* **🛡️ Secure Uplink:** Supports 2FA (Two-Factor Authentication) and persistent session management.
* **📊 Visual Data Mining:** Real-time progress bars with "radar sweep" spinners and data transfer rate monitoring.

---

## 🛠️ INSTALLATION PROTOCOL

### 1. CLONE THE REPOSITORY
Initialize the local environment by cloning the source code.
```bash
git clone [https://github.com/usm007/teleflow-2.0.git](https://github.com/usm007/teleflow-2.0.git)
cd teleflow

```

### 2. INJECT DEPENDENCIES

Install the required Python modules.

```bash
pip install -r requirements.txt

```

---

## 🔐 CONFIGURATION (FIRST RUN)

On the first launch, Teleflow will attempt to establish a secure uplink. You will need your Telegram API credentials.

1. Go to **[my.telegram.org](https://my.telegram.org)**.
2. Log in and select **API development tools**.
3. Create a new application to generate your `API_ID` and `API_HASH`.

When you run the tool, you will see:

```text
[bold red blink]⚠ CREDENTIALS MISSING ⚠
ENTER UPLINK CREDENTIALS:
   >> API_ID:   123456
   >> API_HASH: a1b2c3d4...
   >> PHONE:    +1234567890

```

*These credentials are saved locally to `~/.tbtgdl/credentials.txt`.*

---

## 💀 EXECUTION

To initiate the boot sequence:

```bash
python main.py

```

### CONTROLS

* **Target Selection:** Enter the number of the chat you want to scan (e.g., `1`, `5`).
* **Payload Extraction:** Select files using ranges or single indices:
* `1` (Download file #1)
* `1-5` (Download files #1 through #5)
* `1,3,7` (Download specific files)
* `all` (Download everything)



---

## ⚠️ DISCLAIMER

> **SYSTEM ALERT:** This tool is for **educational purposes only**. The user assumes all responsibility for data exfiltrated using this software. Respect copyright laws and Terms of Service.

---

```

### How to use this:
1.  Create a file named `requirements.txt` and paste the 3 lines of text.
2.  Create a file named `README.md` and paste the markdown content.
3.  Run `pip install -r requirements.txt` in your terminal.
4.  Run 'python main.py'
4.  Run `python main.py` and enjoy your new hacker terminal!

```
