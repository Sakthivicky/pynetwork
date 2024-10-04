import asyncio  
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession()as session:
        async with session.get(url) as response:
            return await response.text()

async def main(urls):
    task=[fetch(url) for url in urls]
    return await asyncio.gather(*task)

if __name__ == "__main__":
    urls = [  # List of URLs to fetch data from
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    
    loop = asyncio.get_event_loop()  
    results = loop.run_until_complete(main(urls))  

    for result in results:  # Print each result
        print(result)