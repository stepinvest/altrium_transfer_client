"""Root object"""
import datetime
from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Message:
    """Root pojo class
    message = Message(
        created=datetime.now(),
        message_type='ic_notification',
        data={'a': 1}
    )
    print(message.to_json())
    """

    created: datetime.datetime
    message_type: str
    data: any
    version: str = "v1"
    ip: str = None
    producer: str = None
    checksum: str = None
    key_id: str = None
