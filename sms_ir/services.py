from typing import List
try :
    import faster_than_requests as requests
except ModuleNotFoundError:
    import requests

response = requests.models.Response

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
    
    def get(self, url, data=None):
        return requests.get(
            url,
            headers=self._headers,
            json=data or {},
        )


class SmsIr(SmsIrRequestMethodMixin):
    ENDPOINT = 'https://api.sms.ir'

    def __init__(
                self,
                api_key: str,
                linenumber: int|None = None,
            ) -> None:
        
        self._linenumber = linenumber
        self._headers = {
            "X-API-KEY": api_key,
            'ACCEPT': 'application/json',
            'Content-Type': 'application/json',
        }

    def send_sms(
                self,
                number: str,
                message: str,
                linenumber: int|None = None,
            ) -> response:
        
        self.send_bulk_sms(
            numbers=[number],
            message=message,
            linenumber=linenumber,
        )

    def send_bulk_sms(
                    self,
                    numbers: List[str],
                    message: str,
                    linenumber: int|None = None,
                ) -> response:
        
        url = f'{self.ENDPOINT}/v1/send/bulk/'

        data = {
            'lineNumber': linenumber or self._linenumber,
            'MessageText': message,
            'Mobiles': numbers,
        }

        return self.post(
            url,
            data,
        )
    
    def send_like_to_like(
                        self,
                        numbers: List[str],
                        messages: List[str],
                        linenumber: int|None =None,
                        send_date_time: str|None =None,
                    ) -> response:
        
        url = f'{self.ENDPOINT}/v1/send/liketolike/'

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

    def delete_scheduled(
                        self,
                        pack_id: int,
                    ) -> response:
        
        url = f'{self.ENDPOINT}/v1/send/scheduled/{pack_id}/'

        return self.delete(
            url,
        )
    
    def send_verify_code(
                        self,
                        number: int,
                        template_id: int,
                        parameters: List,
                    ) -> response:
        
        url = f'{self.ENDPOINT}/v1/send/verify/'

        data = {
            'Mobile' : number,
            'TemplateId' : template_id,
            'Parameters' : parameters,
        }

        return self.post(
            url,
            data,
        )
    
    def report_message(
                    self,
                    message_id: int,
                ) -> response:
        
        url = f'{self.ENDPOINT}/v1/send/{message_id}/'

        return self.get(
            url,
        )
    
    def report_pack(
                    self,
                    pack_id: int,
                ) -> response:
        
        url = f'{self.ENDPOINT}/v1/send/pack/{pack_id}/'

        return self.get(
            url,
        )
    
    def report_today(
                    self,
                    page_size: int,
                    page_number: int,
                ) -> response:
        
        url = f'{self.ENDPOINT}/v1/send/live/'

        data = {
            'pageSize' : page_size,
            'pageNumber' : page_number,
        }

        return self.get(
            url,
            data,
        )
    
    def report_archived(
                        self,
                        from_date: int|None =None,
                        to_date: int|None =None,
                        page_size: int =10,
                        page_number: int =1,
                    ) -> response:

        url = f'{self.ENDPOINT}/v1/send/archive/'

        data = {
            'fromDate': from_date,
            'toDate' : to_date,
            'pageSize' : page_size,
            'pageNumber' : page_number,
        }

        return self.get(
            url,
            data,
        )

    def report_latest_received(
                            self,
                            count: int,
                        ) -> response:
        
        url = f'{self.ENDPOINT}/v1/receive/latest/'

        data = {
            'count': count,
        }

        return self.get(
            url,
            data,
        )
    
    def report_today_received(
                            self,
                            page_size: int,
                            page_number: int,
                        ) -> response:
        
        url = f'{self.ENDPOINT}/v1/receive/live/'

        data = {
            'pageSize': page_size,
            'pageNumber': page_number,
        }

        return self.get(
            url,
            data,
        )
    
    def report_archived_received(
                                self,
                                from_date: int|None =None,
                                to_date: int|None =None,
                                page_size: int =10,
                                page_number: int =1,
                            ) -> response:
        
        url = f'{self.ENDPOINT}/v1/receive/archive/'

        data = {
            'fromDate' : from_date,
            'toDate' : to_date,
            'pageSize' : page_size,
            'pageNumber' : page_number,
        }

        return self.get(
            url,
            data,
        )
    
    def get_credit(self) -> response:
        url = f'{self.ENDPOINT}/v1/credit/'

        return self.get(
            url,
        )

    def get_line_numbers(self) -> response:
        url = f'{self.ENDPOINT}/v1/line/'

        return self.get(
            url,
        )
