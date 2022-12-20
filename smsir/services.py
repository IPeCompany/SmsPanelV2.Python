try :
    import faster_than_requests as requests
except ModuleNotFoundError:
    import requests


class SmsIr :
    ENDPOINT = 'https://api.sms.ir'

    def __init__(self, api_key, linenumber) -> None:
        self._linenumber = linenumber
        self._headers = {
            "X-API-KEY": api_key,
            'ACCEPT': 'application/json',
            'Content-Type': 'application/json',
        }

    def send_sms(self, number, message, linenumber=None):
        self.send_bulk_sms(
            numbers=[number],
            message=message,
            linenumber=linenumber,
        )

    def send_bulk_sms(self, numbers, message, linenumber=None):
        url = f'{self.ENDPOINT}/v1/send/bulk'

        data = {
            'lineNumber': linenumber or self._linenumber,
            'MessageText': message,
            'Mobiles': numbers,
        }

        return self.post(
            url,
            data,
        )

    def post(self, url, data):
        return requests.post(
            url,
            headers=self._headers,
            json=data,
        )