import aiohttp
import asyncio


# for soap api request
async def main():
    async with aiohttp.Clientsession() as session:
        data = '''
        xml data
        '''
        headers = {}
        url = "url"
        # for post request
        async with session.post(url=url, ssl=False, headers=headers,
                                data=data) as resp:
            responded_data = await resp.json()
            print(responded_data)


asyncio.run(main())
