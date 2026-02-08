import os
import sys
import time
import random
import re
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.padding import Padding
from rich.style import Style

console = Console()

# --- ASSETS ---
HACKER_JARGON = [
    "REROUTING_PACKETS", "BRUTE_FORCING_KERNEL", "BYPASSING_FIREWALL_L7", 
    "INJECTING_SQL_PAYLOAD", "SCRUBBING_LOGS", "DECRYPTING_SSL_HANDSHAKE",
    "OVERCLOCKING_CPU_CORES", "SPOOFING_MAC_ADDRESS", "ACCESSING_MAINFRAME",
    "DOWNLOADING_RAM", "TRACING_IP_ROUTE", "DISABLE_ALGORITHMS"
]

ASCII_LOGO = """
  ████████╗███████╗██╗     ███████╗███████╗██╗      ██████╗ ██╗    ██╗
  ╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝██║     ██╔═══██╗██║    ██║
     ██║   █████╗  ██║     █████╗  █████╗  ██║     ██║   ██║██║ █╗ ██║
     ██║   ██╔══╝  ██║     ██╔══╝  ██╔══╝  ██║     ██║   ██║██║███╗██║
     ██║   ███████╗███████╗███████╗██║     ███████╗╚██████╔╝╚███╔███╔╝
     ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝ 
"""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def spacer(lines=1):
    console.print("\n" * lines)

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name)

def random_hex():
    return f"0x{random.randint(4096, 65535):04X}"

def type_writer(text, speed=0.01, style="green"):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(speed)
    print()

def print_header():
    """Prints the main glitchy header."""
    clear_screen()
    console.print(f"[dim]INITIALIZING KERNEL... {random_hex()}[/dim]")
    spacer()
    console.print(Align.center(Text(ASCII_LOGO, style="bold green")))
    # White text on Green background
    console.print(Align.center("[bold white on green]  v3.0_NETRUNNER // ROOT_ACCESS_GRANTED  [/bold white on green]"))
    spacer()

def section_header(title, subtitle=None, style="green"):
    """
    Dramatic section header.
    STRICT FIX: Forces bold white text on the green background.
    """
    spacer()
    
    # 1. The High-Contrast Block (White Text on Green)
    console.print(f"[bold white on {style}]  {title.upper()}  [/bold white on {style}] [dim green]// executing...[/dim green]")
    
    # 2. The Subtitle
    if subtitle:
        console.print(f"[bold white]>> STATUS: {subtitle.upper()}[/bold white]")
    
    spacer()

def fake_log_stream(duration=1.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        msg = random.choice(HACKER_JARGON)
        console.print(f"[dim green]>> {random_hex()} :: {msg}... [OK][/dim green]")
        time.sleep(0.08)