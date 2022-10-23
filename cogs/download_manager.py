from httpx import AsyncClient
import asyncio
from cogs.json_manager import headers
from concurrent.futures import ProcessPoolExecutor


# This is a dictionary to hold the url and path for a download.
downloads = {}

loop_open = True
async def open_download_loop():
    while loop_open:
        if len(downloads) > 0:
            for k,v in downloads.items():
                url = k
                path = v
                async with AsyncClient(headers = headers) as client:
                    r = await client.get(url)
                    with open(path, 'wb') as f:
                        f.write(r.content)
                del downloads[url]

def add_download(**kwargs):
    if loop_open:
        downloads.update({kwargs['url']:kwargs['path']})
    else:
        start_download_loop()
        if loop_open:
            downloads.update({kwargs['url']:kwargs['path']})
        else:
            raise Exception('Download loop failed to start.')


def close_download_loop():
    loop_open = False

def start_download_loop():
    loop_open = True
    with ProcessPoolExecutor() as executor:
        executor.submit(asyncio.run, open_download_loop())
# The add_multiple_downloads function expects a list of dictionaries.
# Each dictionary should have url as the key and path as the value.
def add_multiple_downloads(downloads):
    for download in downloads:
        downloads.update({k,v for k,v in download.items()})
