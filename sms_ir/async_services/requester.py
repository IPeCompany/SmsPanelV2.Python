from aiohttp import ClientSession, ClientResponse

from ..base_requester import BaseRequester


class Requestser(BaseRequester):
    def __init__(self, headers: dict[str, str]) -> None:
        super().__init__()
        self._session = ClientSession(base_url=self.endpoint, headers=headers)
        
    async def close(self):
        await self._session.close()

    async def post(self, url: str, json) -> ClientResponse:
        self.logger.info(f"send request to {url}")
        return await self._session.post(
            url,
            json=json,
        )

    async def delete(self, url: str) -> ClientResponse:
        self.logger.info(f"send request to {url}")
        return await self._session.delete(
            url,
        )

    async def get(self, url: str, params=None) -> ClientResponse:
        self.logger.info(f"send request to {url}")
        return await self._session.get(
            url,
            params=params,
        )
