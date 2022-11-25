"""Transfer POJO classes"""

# import json
from dataclasses import dataclass
from typing import Any


@dataclass
class AmtDtls:
    txnCcy: str
    txnAmt: float

    @staticmethod
    def from_dict(obj: Any) -> "AmtDtls":
        _txnCcy = str(obj.get("txnCcy"))
        _txnAmt = float(obj.get("txnAmt"))
        return AmtDtls(_txnCcy, _txnAmt)


@dataclass
class Header:
    msgId: str
    orgId: str
    timeStamp: str
    ctry: str

    @staticmethod
    def from_dict(obj: Any) -> "Header":
        _msgId = str(obj.get("msgId"))
        _orgId = str(obj.get("orgId"))
        _timeStamp = str(obj.get("timeStamp"))
        _ctry = str(obj.get("ctry"))
        return Header(_msgId, _orgId, _timeStamp, _ctry)


@dataclass
class ReceivingParty:
    name: str
    accountNo: str
    virtualAccountNo: str

    @staticmethod
    def from_dict(obj: Any) -> "ReceivingParty":
        _name = str(obj.get("name"))
        _accountNo = str(obj.get("accountNo"))
        _virtualAccountNo = str(obj.get("virtualAccountNo"))
        return ReceivingParty(_name, _accountNo, _virtualAccountNo)


@dataclass
class RmtInf:
    paymentDetails: str

    @staticmethod
    def from_dict(obj: Any) -> "RmtInf":
        _paymentDetails = str(obj.get("paymentDetails"))
        return RmtInf(_paymentDetails)


@dataclass
class SenderParty:
    name: str
    accountNo: str
    senderBankId: str

    @staticmethod
    def from_dict(obj: Any) -> "SenderParty":
        _name = str(obj.get("name"))
        _accountNo = str(obj.get("accountNo"))
        _senderBankId = str(obj.get("senderBankId"))
        return SenderParty(_name, _accountNo, _senderBankId)


@dataclass
class TxnInfo:
    txnType: str
    customerReference: str
    txnRefId: str
    txnDate: str
    valueDt: str
    receivingParty: ReceivingParty
    amtDtls: AmtDtls
    senderParty: SenderParty
    rmtInf: RmtInf

    @staticmethod
    def from_dict(obj: Any) -> "TxnInfo":
        _txnType = str(obj.get("txnType"))
        _customerReference = str(obj.get("customerReference"))
        _txnRefId = str(obj.get("txnRefId"))
        _txnDate = str(obj.get("txnDate"))
        _valueDt = str(obj.get("valueDt"))
        _receivingParty = ReceivingParty.from_dict(obj.get("receivingParty"))
        _amtDtls = AmtDtls.from_dict(obj.get("amtDtls"))
        _senderParty = SenderParty.from_dict(obj.get("senderParty"))
        _rmtInf = RmtInf.from_dict(obj.get("rmtInf"))
        return TxnInfo(
            _txnType,
            _customerReference,
            _txnRefId,
            _txnDate,
            _valueDt,
            _receivingParty,
            _amtDtls,
            _senderParty,
            _rmtInf,
        )


@dataclass
class ICNotification:
    header: Header
    txnInfo: TxnInfo

    @staticmethod
    def from_dict(obj: Any) -> "ICNotification":
        _header = Header.from_dict(obj.get("header"))
        _txnInfo = TxnInfo.from_dict(obj.get("txnInfo"))
        return ICNotification(_header, _txnInfo)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
