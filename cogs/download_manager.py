from httpx import AsyncClient
import asyncio
from cogs.json_manager import headers



# This is a dictionary to hold the url and path for a download.
downloads = {}

loop_open = True
async def open_download_loop():
    while loop_open:
        for k,v in downloads.items():
            url = k
            path = v
            async with AsyncClient(headers = headers) as client:
                r = await client.get(url)
                with open(path, 'wb') as f:
                    f.write(r.content)
            del downloads[url]

def add_download(**kwargs):
    downloads.update({kwargs['url']:kwargs['path']})

