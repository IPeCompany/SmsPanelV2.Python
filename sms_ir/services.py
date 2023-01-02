from typing import List
from requests.models import Response
from .mixins import RequestsMixin, LoggerMixin


class SmsIr(RequestsMixin, LoggerMixin):
    ENDPOINT = 'https://api.sms.ir'

    def __init__(
                self,
                api_key: str,
                linenumber: int|None = None,
            ) -> None:
        
        self.config_logger()
        
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
            ) -> Response:
        """
        Send message to specific mobile number
        """
        
        return self.send_bulk_sms(
            numbers=[number],
            message=message,
            linenumber=linenumber,
        )

    def send_bulk_sms(
                    self,
                    numbers: List[str],
                    message: str,
                    linenumber: int|None = None,
                ) -> Response:
        """
        Send message to multiple mobile numbers
        """
        
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
                    ) -> Response:
        """
        Send multiple messages to multiple mobile numbers pair to pair
        """
        
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
                    ) -> Response:
        """
        Delete scheduled message pack
        """
        
        url = f'{self.ENDPOINT}/v1/send/scheduled/{pack_id}/'

        return self.delete(
            url,
        )
    
    def send_verify_code(
                        self,
                        number: int,
                        template_id: int,
                        parameters: List,
                    ) -> Response:
        """
        Send verification code with predefined template
        """
        
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
                ) -> Response:
        """
        get report of sent message
        """
        
        url = f'{self.ENDPOINT}/v1/send/{message_id}/'

        return self.get(
            url,
        )
    
    def report_pack(
                    self,
                    pack_id: int,
                ) -> Response:
        """
        get report of sent message pack
        """
        
        url = f'{self.ENDPOINT}/v1/send/pack/{pack_id}/'

        return self.get(
            url,
        )
    
    def report_today(
                    self,
                    page_size: int =10,
                    page_number: int =1,
                ) -> Response:
        """
        get report of Today sent Messages
        """
        
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
                    ) -> Response:
        """
        get report of Archived Messages
        """

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
                        ) -> Response:
        """
        get report of latest received messages
        """
        
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
                            page_size: int =10,
                            page_number: int =1,
                        ) -> Response:
        """
        get report of today received messages
        """
        
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
                            ) -> Response:
        """
        get report of today received messages
        """
        
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
    
    def get_credit(self) -> Response:
        """
        get account credit
        """

        url = f'{self.ENDPOINT}/v1/credit/'

        return self.get(
            url,
        )

    def get_line_numbers(self) -> Response:
        """
        get account line numbers
        """

        url = f'{self.ENDPOINT}/v1/line/'

        return self.get(
            url,
        )
