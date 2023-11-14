import time
import asyncio
from desktop_notifier import DesktopNotifier


while True:
    time.sleep(3600)

    async def main():
        notifier = DesktopNotifier()
        await notifier.send(title="Drink Water!", message="Hey Trishan, it's time to drink water!")
    asyncio.run(main())
