"""Client pojo test"""
import json
import os
import unittest
from datetime import datetime
from pathlib import Path

from transfer_client.messages import Message
from transfer_client.v1.icn import ICNotification


class ICNPojoTest(unittest.TestCase):
    """ICN Pojo Tests"""

    def setUp(self) -> None:
        self.base_path = Path(__file__).resolve().parent
        self.transfer_req = open(
            os.path.join(self.base_path, "data/transfer_req_va.json")
        ).read()

    def test_deserialization(self):
        """Test json deserialization"""
        icn_notification = ICNotification.from_dict(json.loads(self.transfer_req))
        self.assertIsNotNone(icn_notification)
        self.assertEqual(icn_notification.header.msgId, "2021012715291620210127")


class MessageTest(unittest.TestCase):
    """ICN Pojo Tests"""

    def setUp(self) -> None:
        self.base_path = Path(__file__).resolve().parent
        self.transfer_req = open(
            os.path.join(self.base_path, "data/transfer_req_va.json")
        ).read()

    def test_message_loading(self):
        """Test message loading"""
        icn_notification = ICNotification.from_dict(json.loads(self.transfer_req))
        self.assertIsNotNone(icn_notification)
        self.assertEqual(icn_notification.header.msgId, "2021012715291620210127")
        message = Message(
            created=datetime.now(),
            message_type="icn_notification",
            data=icn_notification,
        )
        json_str = message.to_json()
        self.assertIsNotNone(json_str)

    def test_message_unloading(self):
        """Test message loading."""
        json_str = '{"created": 1671015409.828648, "message_type": "icn_notification", "data": {"header": \
            {"msgId": "2021012715291620210127", "orgId": "ORGID001", "timeStamp": "2021-01-27T12:59:16.532", \
                "ctry": "SG"},  "txnInfo": {"txnType": "INCOMING ACT", "customerReference": "REF00001", \
                    "txnRefId": "0811RF0600123", "txnDate": "2021-01-27", "valueDt": "2021-01-27", \
                "receivingParty": {"name": "Bene", "accountNo": "01234567891", "virtualAccountNo": \
                    "9ACV12345"}, "amtDtls": {"txnCcy": "SGD", "txnAmt": 1.2}, "senderParty": \
                        {"name": "Sender", "accountNo": "08987877868", "senderBankId": "DBSSSGXX"}, \
                            "rmtInf": {"paymentDetails": "Testing IDN"}}, "keyId": null}, \
                                "version": "v1", "checksum": null}'
        message = Message.from_json(json_str)
        self.assertIsNotNone(message)
        ic_notification = ICNotification.from_dict(message.data)
        self.assertIsNotNone(ic_notification.header)
        self.assertEqual(ic_notification.header.msgId, "2021012715291620210127")
