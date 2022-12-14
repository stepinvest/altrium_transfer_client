"""Root object"""
import datetime
from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Message:
    """Root pojo class"""

    created: datetime.datetime
    message_type: str
    data: any
    version: str = "v1"
    checksum: str = None
