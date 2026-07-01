from pydantic import BaseModel, Field
from typing import Optional


class PaymentRequest(BaseModel):
    customer_id: str = Field(..., min_length=3, max_length=30)
    beneficiary_account: str = Field(..., min_length=8, max_length=20)
    ifsc_code: Optional[str] = Field(default=None, max_length=11)
    upi_id: Optional[str] = Field(default=None, max_length=80)
    amount: float = Field(..., gt=0, le=200000)
    remarks: Optional[str] = Field(default="Payment initiated", max_length=120)


class PaymentResponse(BaseModel):
    transaction_id: str
    payment_mode: str
    status: str
    amount: float
    message: str


class TransactionStatus(BaseModel):
    transaction_id: str
    payment_mode: str
    status: str
    amount: float
    customer_id: str
    remarks: str
