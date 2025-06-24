"""Entry point demonstrating memory, NLP and GGUF model integration."""

from __future__ import annotations

import asyncio

from backup import BackupManager
from memory_ import Memory
from models.gguf_loader import GGUFModel
from nlp.dialogue_manager import DialogueManager
from scheduler import Scheduler
from modules.offline_mode import OfflineMode
from modules.voice_assistant import listen, speak


async def main() -> None:
    memory = Memory()
    offline = OfflineMode()
    try:
        model = None if offline.active else GGUFModel("models/sample.gguf")
    except Exception:
        model = None
    dialog = DialogueManager(memory, model=model)
    backup_manager = BackupManager(memory)

    scheduler = Scheduler()
    scheduler.schedule(backup_interval := 10, backup_manager.backup, name="backup")

    print("Type something (ctrl+c to exit)...")
    try:
        while True:
            user_in = listen() if not offline.active else input("> ")
            reply = dialog.handle_input(user_in)
            speak(reply)
    except KeyboardInterrupt:
        print("\nExiting...")

    # Backup once more on exit
    await backup_manager.backup()


if __name__ == "__main__":
    asyncio.run(main())
