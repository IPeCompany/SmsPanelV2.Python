# smsir-python
sms.ir python package

## Installation
```
pip install smsir-python
```

## Requirements
You only need the requests package to send apis.

## Usage
### Create Instance
```python
from sms_ir import SmsIr
sms_ir = SmsIr(
    api_key,
    linenumber,
)
```

### Send Sms
Send message to specific mobile number
```python
sms_ir.send_sms(
    number,
    message,
    linenumber,
)
```

### Send Bulk Sms
Send message to multiple mobile numbers
```python
sms_ir.send_bulk_sms(
    numbers,
    message,
    linenumber,
)
```

### Send Like To Like Sms
Send multiple messages to multiple mobile numbers pair to pair
```python
sms_ir.send_like_to_like(
    numbers,
    messages,
    linenumber,
    send_date_time,
)
```

### Delete Scheduled
Delete scheduled message pack
```python
sms_ir.delete_scheduled(
    pack_id,
)
```

### Send Verification Code
Send verification code with predefined template
```python
sms_ir.send_verify_code(
    number,
    template_id,
    parameters,
)
```
another sample code:
```python
sms_ir.send_verify_code(
    number="+989111111111",
    template_id=10000,
    parameters=[
        {
            "name" : "code",
            "value": 12345,
        },
    ],
)
```

### Message Report
get report of sent message
```python
sms_ir.report_message(
    message_id,
)
```

### Pack Report
get report of sent message pack
```python
sms_ir.report_pack(
    pack_id,
)
```

### Today Report
get report of Today sent Messages
```python
sms_ir.report_today(
    page_size,
    page_number,
)
```

### Archived Report
get report of Archived Messages
```python
sms_ir.report_archived(
    from_date,
    to_date,
    page_size,
    page_number,
)
```

### Latest Received Report
get report of latest received messages
```python
sms_ir.report_latest_received(
    count,
)
```

### Today Received Report
get report of today received messages
```python
sms_ir.report_today_received(
    page_size,
    page_number,
)
```

### Archived Received Report
get report of today received messages
```python
sms_ir.report_archived_received(
    from_date,
    to_date,
    page_size,
    page_number,
)
```

### Get Credit
get account credit
```python
sms_ir.get_credit()
```

### Get Line Numbers
get account line numbers
```python
sms_ir.get_line_numbers()
```

## Link
If you find a bug or have a question, you can contact me via the link below mojtaba.akbari.221B@gmail.com.
