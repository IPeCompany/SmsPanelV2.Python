import requests
from requests import RequestException

from ..base_requester import BaseRequester


class Requestser(BaseRequester):
    def __init__(self, headers: dict[str, str]) -> None:
        super().__init__()
        self._session = requests.Session()
        self._session.headers.update(headers)

    def post(self, url: str, json):
        try:
            url = self.endpoint + url
            self.logger.info("send request to %s", url)
            return self._session.post(
                url,
                json=json,
            )
        except RequestException as e:
            self.logger.error(str(e))
            return self.fake_response(e.request)

    def delete(self, url: str):
        try:
            url = self.endpoint + url
            self.logger.info("send request to %s", url)
            return self._session.delete(url)
        except RequestException as e:
            self.logger.error(str(e))
            return self.fake_response(e.request)

    def get(self, url: str, params=None):
        try:
            url = self.endpoint + url
            self.logger.info("send request to %s", url)
            return self._session.get(
                url,
                params=params,
            )
        except RequestException as e:
            self.logger.error(str(e))
            return self.fake_response(e.request)

    def fake_response(self, request):
        response = requests.models.Response()

        response.status_code = 503
        response.request = request
        response.url = request.url

        return response
