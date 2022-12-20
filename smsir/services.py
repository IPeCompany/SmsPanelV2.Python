try :
    import faster_than_requests as requests
except ModuleNotFoundError:
    import requests


class SmsIrRequestMethodMixin :
    def post(self, url, data):
        return requests.post(
            url,
            headers=self._headers,
            json=data,
        )

    def delete(self, url):
        return requests.delete(
            url,
            headers=self._headers,
        )

class SmsIr(SmsIrRequestMethodMixin):
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
    
    def send_like_to_like(self, numbers, messages, linenumber=None, send_date_time=None):
        url = f'{self.ENDPOINT}/v1/send/liketolike'

        data = {
            'lineNumber': linenumber or self._linenumber,
            'MessageTexts' : messages,
            'Mobiles': numbers,
            'SendDateTime': send_date_time,
        }

        return self.post(
            url,
            data,
        )

    def delete_scheduled(self, pack_id):
        url = f'{self.ENDPOINT}/v1/send/scheduled/{pack_id}'

        return self.delete(
            url,
        )