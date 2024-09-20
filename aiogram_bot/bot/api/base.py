import aiohttp

from config.settings import Settings

class BaseAPI:


    base_url = ''

    async def request(self, url, json={}, params={}, method='GET'):
        async with aiohttp.ClientSession() as session:
            async with session.request(method=method, headers={
                'Authorization': f'EnvToken {Settings().api_token}'
            }, url=self.base_url + url, json=json, params=params) as response:

                if response.status == 429:
                    raise Exception(429)


                if response.status >= 300 or response.status < 200:
                    raise Exception(str(await response.json()) + f" {url=}")
                await response.json()
                return response
