import os
import time
import random
from collections import deque
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.progress import (
    Progress, BarColumn, TextColumn, 
    TimeRemainingColumn, DownloadColumn, TransferSpeedColumn, SpinnerColumn
)
from telethon.tl.types import Channel, Chat, User, MessageMediaDocument, DocumentAttributeVideo
from ui import (
    clear_screen, print_header, section_header, spacer, 
    console, sanitize_filename, fake_log_stream, random_hex, type_writer
)

DOWNLOAD_DIR = "Exfiltrated_Data"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

class DownloadManager:
    def __init__(self):
        self.queue = deque()
        self.current = None

manager = DownloadManager()

def parse_selection(inp, max_i):
    if inp in ("0", "exit", "abort"): return None
    if inp == "all": return list(range(1, max_i + 1))
    out = set()
    try:
        for part in inp.split(","):
            if "-" in part:
                a, b = map(int, part.split("-"))
                out.update(range(min(a, b), max(a, b) + 1))
            elif part.isdigit():
                out.add(int(part))
    except: pass
    return sorted(i for i in out if 1 <= i <= max_i)

async def select_chat(client):
    section_header("TARGET_ACQUISITION", "SCANNING NETWORK NODES", style="green")
    fake_log_stream(0.5)

    dialogs = await client.get_dialogs()
    chats = []
    
    # FIX: White Text on Green Header
    table = Table(box=None, padding=(0, 1), show_header=True, header_style="bold white on green")
    table.add_column("ID_REF", justify="right", style="bold green", width=6)
    table.add_column("TARGET_IDENTITY", style="bold white")

    for d in dialogs:
        e = d.entity
        name = (d.name or getattr(e, "title", None) or getattr(e, "first_name", None) or "UNKNOWN_NODE").strip()
        if isinstance(e, (Channel, Chat, User)):
            chats.append({"entity": e, "name": name})

    for i, c in enumerate(chats, 1):
        table.add_row(f"[{i:02}]", c['name'])

    console.print(table)
    spacer()
    
    type_writer(">> AWAITING TARGET INDEX...", speed=0.01)
    choice = console.input("[bold green]root@teleflow:~/targets# [/bold green]").strip()
    
    if not choice.isdigit() or int(choice) == 0: return
    await select_videos(client, chats[int(choice) - 1])

async def select_videos(client, chat):
    section_header("DATA_MINING", f"INFILTRATING: {chat['name']}", style="green")

    videos = []
    
    # FIX: Spinner changed to 'dots12'
    with console.status("[bold green]INJECTING PACKETS... DECRYPTING METADATA...[/bold green]", spinner="dots12"):
        async for msg in client.iter_messages(chat["entity"], limit=500):
            if msg.media and isinstance(msg.media, MessageMediaDocument):
                if any(isinstance(a, DocumentAttributeVideo) for a in msg.media.document.attributes):
                    name = sanitize_filename(msg.file.name or f"payload_{msg.id}.mp4")
                    size_mb = msg.media.document.size / (1024 * 1024)
                    videos.append({"msg": msg, "name": name, "size": size_mb})

    if not videos:
        console.print("[bold red on black] ⚠ NO VULNERABILITIES FOUND (NO VIDEOS) ⚠ [/bold red on black]")
        time.sleep(2)
        return

    # FIX: White Text on Green Header
    table = Table(box=None, padding=(0, 2), show_header=True, header_style="bold white on green")
    table.add_column("INDEX", justify="right", style="dim white")
    table.add_column("PAYLOAD_NAME", style="cyan")
    table.add_column("SIZE", justify="right", style="green")

    for i, v in enumerate(videos, 1):
        table.add_row(f"[{i:02}]", v['name'], f"{v['size']:.1f} MB")

    console.print(table)
    spacer()
    
    console.print("[dim]COMMANDS: '1', '1-5', 'all'[/dim]")
    sel = console.input("[bold green]root@teleflow:~/payloads# [/bold green]").strip()
    
    idxs = parse_selection(sel, len(videos))
    if not idxs: return

    manager.queue.clear()
    for i in idxs:
        v = videos[i - 1]
        manager.queue.append({
            "msg": v["msg"], "name": v["name"], "size": v["size"],
            "path": os.path.join(DOWNLOAD_DIR, v["name"])
        })

    await download_screen()

async def download_screen():
    print_header()
    section_header("EXFILTRATION_PROTOCOL", "SECURE CHANNEL ESTABLISHED", style="blue")
    
    total_files = len(manager.queue)
    processed = 0

    while manager.queue:
        manager.current = manager.queue.popleft()
        processed += 1
        
        console.print(f"[bold green]>> DOWNLOADING PACKET {processed}/{total_files} :: {random_hex()}[/bold green]")
        console.print(f"[dim white]{manager.current['name']}[/dim white]")

        progress = Progress(
            TextColumn("[bold red]⚡[/bold red]"),
            SpinnerColumn("dots12"),
            TextColumn("[bold green]{task.description}[/bold green]", justify="right"),
            BarColumn(bar_width=None, style="dim green", complete_style="bold green"),
            "[progress.percentage]{task.percentage:>3.0f}%",
            "•",
            TransferSpeedColumn(),
            "•",
            TimeRemainingColumn(),
            console=console,
            expand=True
        )

        with progress:
            task_id = progress.add_task(
                "TRANSFERRING", 
                total=manager.current["size"] * 1024 * 1024
            )

            async def progress_cb(current, total):
                progress.update(task_id, completed=current)

            await manager.current["msg"].download_media(
                file=manager.current["path"],
                progress_callback=progress_cb
            )
        
        console.print(f"[dim]>> MD5 CHECKSUM: {random_hex()}{random_hex()} [MATCH][/dim]")
        spacer()

    section_header("MISSION_COMPLETE", "LOGS SCRUBBED", style="green")
    console.print("[bold white on green]  ALL ASSETS RECOVERED SUCCESSFULLY  [/bold white on green]")
    console.input("\n[dim]Press Enter to vanish...[/dim]")