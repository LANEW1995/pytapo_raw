# save as grab.py (or just paste into a shell one-liner)
import asyncio, time
from pytapo import Tapo
from downloader import Downloader          # path: <repo_root>/downloader.py

async def main():
    cam = Tapo("10.0.0.151", "lanew1995", "People22!")  # IP, username, password

    # Grab the last 30 seconds
    end   = int(time.time())
    start = end - 30

    dl = Downloader(
        tapo           = cam,
        startTime      = start,
        endTime        = end,
        timeCorrection = 0,
        outputDirectory= "./captures/",    # make sure it exists
    )

    status = await dl.downloadFile(print)  # prints progress callbacks
    print("\nDone →", status["fileName"])

asyncio.run(main())
