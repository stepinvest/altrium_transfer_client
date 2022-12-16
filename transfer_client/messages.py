"""Root object"""
import datetime
from dataclasses import dataclass
from typing import Optional

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
    data: dataclass
    version: str = "v1"
    ip: Optional[str] = None
    producer: Optional[str] = None
    checksum: Optional[str] = None
    key_id: Optional[str] = None
