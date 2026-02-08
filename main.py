import asyncio
import time
import random
from rich.console import Console
from telegram import get_telegram_client
from downloader import select_chat
from ui import print_header, fake_log_stream, spacer

console = Console()

async def boot_sequence():
    """Simulates a movie-style boot sequence."""
    # Clear screen command
    print("\033c", end="")
    
    # Fast scrolling text
    modules = ["KERNEL", "MEMORY", "NETWORK", "CRYPTO", "UI_SYSTEM"]
    for mod in modules:
        console.print(f"[green]>> LOADING {mod} MODULE...[/green] [bold white]OK[/bold white]")
        time.sleep(random.uniform(0.05, 0.2))
    
    fake_log_stream(1.0)
    spacer()
    console.print("[bold cyan]SYSTEM READY.[/bold cyan]")
    time.sleep(0.5)

async def main():
    try:
        await boot_sequence()
        client = await get_telegram_client()
        if not client: return

        async with client:
            while True:
                await select_chat(client)
    except KeyboardInterrupt:
        console.print("\n[bold red]>> CONNECTION TERMINATED BY USER.[/bold red]")
    except Exception as e:
        console.print_exception()
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    asyncio.run(main())