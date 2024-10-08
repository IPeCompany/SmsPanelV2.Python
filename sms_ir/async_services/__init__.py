from typing import List, Optional

from aiohttp import ClientResponse

from .requester import Requestser

class AsyncSmsIr:
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
        
    async def close(self):
        """
        Close the session connection
        """
        await self._requester.close()
        
    async def send_sms(
        self,
        number: str,
        message: str,
        linenumber: Optional[int] = None,
    ) -> ClientResponse:
        """
        Send message to specific mobile number
        """

        return await self.send_bulk_sms(
            numbers=[number],
            message=message,
            linenumber=linenumber,
        )

    async def send_bulk_sms(
        self,
        numbers: List[str],
        message: str,
        linenumber: Optional[int] = None,
    ) -> ClientResponse:
        """
        Send message to multiple mobile numbers
        """

        url = "/v1/send/bulk/"

        data = {
            "lineNumber": linenumber or self._linenumber,
            "MessageText": message,
            "Mobiles": numbers,
        }

        return await self._requester.post(
            url,
            data,
        )

    async def send_like_to_like(
        self,
        numbers: List[str],
        messages: List[str],
        linenumber: Optional[int] = None,
        send_date_time: Optional[str] = None,
    ) -> ClientResponse:
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

        return await self._requester.post(
            url,
            data,
        )

    async def delete_scheduled(
        self,
        pack_id: int,
    ) -> ClientResponse:
        """
        Delete scheduled message pack
        """

        url = f"/v1/send/scheduled/{pack_id}/"

        return await self._requester.delete(
            url,
        )

    async def send_verify_code(
        self,
        number: str,
        template_id: int,
        **parameters: dict[str, str],
    ) -> ClientResponse:
        """
        Send verification code with preasync defined template
        """

        url = "/v1/send/verify/"

        data = {
            "Mobile": number,
            "TemplateId": template_id,
            "Parameters": [dict(name=k, value=v) for k, v in parameters.items()],
        }

        return await self._requester.post(
            url,
            data,
        )

    async def report_message(
        self,
        message_id: int,
    ) -> ClientResponse:
        """
        get report of sent message
        """

        url = f"/v1/send/{message_id}/"

        return await self._requester.get(
            url,
        )

    async def report_pack(
        self,
        pack_id: int,
    ) -> ClientResponse:
        """
        get report of sent message pack
        """

        url = f"/v1/send/pack/{pack_id}/"

        return await self._requester.get(
            url,
        )

    async def report_today(
        self,
        page_size: int = 10,
        page_number: int = 1,
    ) -> ClientResponse:
        """
        get report of Today sent Messages
        """

        url = "/v1/send/live/"

        params = {
            "pageSize": page_size,
            "pageNumber": page_number,
        }

        return await self._requester.get(
            url,
            params,
        )

    async def report_archived(
        self,
        from_date: Optional[int] = None,
        to_date: Optional[int] = None,
        page_size: int = 10,
        page_number: int = 1,
    ) -> ClientResponse:
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

        return await self._requester.get(
            url,
            params,
        )

    async def report_latest_received(
        self,
        count: int,
    ) -> ClientResponse:
        """
        get report of latest received messages
        """

        url = "/v1/receive/latest/"

        params = {
            "count": count,
        }

        return await self._requester.get(
            url,
            params,
        )

    async def report_today_received(
        self,
        page_size: int = 10,
        page_number: int = 1,
    ) -> ClientResponse:
        """
        get report of today received messages
        """

        url = "/v1/receive/live/"

        params = {
            "pageSize": page_size,
            "pageNumber": page_number,
        }

        return await self._requester.get(
            url,
            params,
        )

    async def report_archived_received(
        self,
        from_date: Optional[int] = None,
        to_date: Optional[int] = None,
        page_size: int = 10,
        page_number: int = 1,
    ) -> ClientResponse:
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

        return await self._requester.get(
            url,
            params,
        )

    async def get_credit(self) -> ClientResponse:
        """
        get account credit
        """

        url = "/v1/credit/"

        return await self._requester.get(
            url,
        )

    async def get_line_numbers(self) -> ClientResponse:
        """
        get account line numbers
        """

        url = "/v1/line/"

        return await self._requester.get(
            url,
        )

