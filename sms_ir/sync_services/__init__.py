from typing import List, Optional
from requests.models import Response
from .requester import Requestser


class SmsIr:
    def __init__(
        self,
        api_key: str,
        linenumber: Optional[int] = None,
    ) -> None:
        headers = {
            "X-API-KEY": api_key,
            "ACCEPT": "application/json",
            "Content-Type": "application/json",
        }

        self._linenumber = linenumber
        self._requester = Requestser(headers)

    def send_sms(
        self,
        number: str,
        message: str,
        linenumber: Optional[int] = None,
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
        linenumber: Optional[int] = None,
    ) -> Response:
        """
        Send message to multiple mobile numbers
        """

        url = "/v1/send/bulk/"

        data = {
            "lineNumber": linenumber or self._linenumber,
            "MessageText": message,
            "Mobiles": numbers,
        }

        return self._requester.post(
            url,
            data,
        )

    def send_like_to_like(
        self,
        numbers: List[str],
        messages: List[str],
        linenumber: Optional[int] = None,
        send_date_time: Optional[str] = None,
    ) -> Response:
        """
        Send multiple messages to multiple mobile numbers pair to pair
        """

        url = "/v1/send/liketolike/"

        data = {
            "lineNumber": linenumber or self._linenumber,
            "MessageTexts": messages,
            "Mobiles": numbers,
            "SendDateTime": send_date_time,
        }

        return self._requester.post(
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

        url = f"/v1/send/scheduled/{pack_id}/"

        return self._requester.delete(
            url,
        )

    def send_verify_code(
        self,
        number: str,
        template_id: int,
        **parameters: str,
    ) -> Response:
        """
        Send verification code with predefined template
        """

        url = "/v1/send/verify/"

        data = {
            "Mobile": number,
            "TemplateId": template_id,
            "Parameters": [dict(name=k, value=v) for k, v in parameters.items()],
        }

        return self._requester.post(
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

        url = f"/v1/send/{message_id}/"

        return self._requester.get(
            url,
        )

    def report_pack(
        self,
        pack_id: int,
    ) -> Response:
        """
        get report of sent message pack
        """

        url = f"/v1/send/pack/{pack_id}/"

        return self._requester.get(
            url,
        )

    def report_today(
        self,
        page_size: int = 10,
        page_number: int = 1,
    ) -> Response:
        """
        get report of Today sent Messages
        """

        url = "/v1/send/live/"

        params = {
            "pageSize": page_size,
            "pageNumber": page_number,
        }

        return self._requester.get(
            url,
            params,
        )

    def report_archived(
        self,
        from_date: Optional[int] = None,
        to_date: Optional[int] = None,
        page_size: int = 10,
        page_number: int = 1,
    ) -> Response:
        """
        get report of Archived Messages
        """

        url = "/v1/send/archive/"

        params = {
            "fromDate": from_date,
            "toDate": to_date,
            "pageSize": page_size,
            "pageNumber": page_number,
        }

        return self._requester.get(
            url,
            params,
        )

    def report_latest_received(
        self,
        count: int,
    ) -> Response:
        """
        get report of latest received messages
        """

        url = "/v1/receive/latest/"

        params = {
            "count": count,
        }

        return self._requester.get(
            url,
            params,
        )

    def report_today_received(
        self,
        page_size: int = 10,
        page_number: int = 1,
    ) -> Response:
        """
        get report of today received messages
        """

        url = "/v1/receive/live/"

        params = {
            "pageSize": page_size,
            "pageNumber": page_number,
        }

        return self._requester.get(
            url,
            params,
        )

    def report_archived_received(
        self,
        from_date: Optional[int] = None,
        to_date: Optional[int] = None,
        page_size: int = 10,
        page_number: int = 1,
    ) -> Response:
        """
        get report of today received messages
        """

        url = "/v1/receive/archive/"

        params = {
            "fromDate": from_date,
            "toDate": to_date,
            "pageSize": page_size,
            "pageNumber": page_number,
        }

        return self._requester.get(
            url,
            params,
        )

    def get_credit(self) -> Response:
        """
        get account credit
        """

        url = "/v1/credit/"

        return self._requester.get(
            url,
        )

    def get_line_numbers(self) -> Response:
        """
        get account line numbers
        """

        url = "/v1/line/"

        return self._requester.get(
            url,
        )
