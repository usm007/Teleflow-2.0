import os
import ctypes
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from ui import console, section_header, spacer, clear_screen, print_header, fake_log_stream, type_writer

SESSION_NAME = "video_downloader"
SESSION_FILE = f"{SESSION_NAME}.session"
BASE_DIR = os.path.expanduser("~/.tbtgdl")
os.makedirs(BASE_DIR, exist_ok=True)
CRED_FILE = os.path.join(BASE_DIR, "credentials.txt")

def hide_file(path):
    if os.name == "nt":
        try: ctypes.windll.kernel32.SetFileAttributesW(path, 0x02)
        except: pass

def load_credentials():
    if not os.path.exists(CRED_FILE): return None, None, None
    with open(CRED_FILE, "r") as f:
        lines = [l.strip() for l in f.readlines()]
    return (int(lines[0]), lines[1], lines[2]) if len(lines) >= 3 else (None, None, None)

async def get_telegram_client():
    print_header()
    section_header("AUTHENTICATION", "BIOMETRIC SCAN REQUIRED", style="green")
    
    api_id, api_hash, phone = load_credentials()
    
    if not api_id:
        console.print("[bold red blink]⚠ CREDENTIALS MISSING ⚠[/bold red blink]")
        fake_log_stream(1)
        spacer()
        
        console.print("[bold white]ENTER UPLINK CREDENTIALS:[/bold white]")
        api_id = int(console.input("   [green]>> API_ID:   [/green] "))
        api_hash = console.input("   [green]>> API_HASH: [/green] ")
        phone = console.input("   [green]>> PHONE:    [/green] ")
        
        with open(CRED_FILE, "w") as f: f.write(f"{api_id}\n{api_hash}\n{phone}")
        hide_file(CRED_FILE)
        spacer()

    client = TelegramClient(SESSION_NAME, api_id, api_hash)
    await client.connect()

    if not await client.is_user_authorized():
        console.print("[dim]REQUESTING ONE-TIME PAD...[/dim]")
        await client.send_code_request(phone)
        
        spacer()
        type_writer(">> SECURE CHANNEL OPEN. WAITING FOR INPUT.", speed=0.03)
        code = console.input("   [bold green]>> ENTER OTP: [/bold green]")
        
        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            spacer()
            console.print("[bold red on white] ⚠ LEVEL 5 SECURITY DETECTED ⚠ [/bold red on white]")
            pwd = console.input("   [red]>> ENTER MASTER PASSWORD: [/red]", password=True)
            await client.sign_in(password=pwd)

    hide_file(SESSION_FILE)
    
    spacer()
    # FIX: White text on Green
    console.print("[bold white on green]  ACCESS GRANTED  [/bold white on green]")
    await asyncio.sleep(1)
    
    return client