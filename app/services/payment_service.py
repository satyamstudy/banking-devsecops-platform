import uuid
from typing import Dict, Optional

from app.models import PaymentRequest, PaymentResponse, TransactionStatus


class PaymentService:
    """Mock service for banking payment workflows.

    This project is focused on DevOps and deployment automation, so the data store
    is intentionally in-memory. In a real system, transactions would be stored in
    a database and integrated with payment gateways or banking rails.
    """

    def __init__(self):
        self.transactions: Dict[str, TransactionStatus] = {}

    def create_payment(self, payment_mode: str, request: PaymentRequest) -> PaymentResponse:
        self._validate_payment_mode(payment_mode, request)

        transaction_id = f"TXN-{uuid.uuid4().hex[:12].upper()}"
        status = "SUCCESS" if request.amount <= 100000 else "PENDING_REVIEW"

        transaction = TransactionStatus(
            transaction_id=transaction_id,
            payment_mode=payment_mode,
            status=status,
            amount=request.amount,
            customer_id=request.customer_id,
            remarks=request.remarks or "Payment initiated",
        )
        self.transactions[transaction_id] = transaction

        return PaymentResponse(
            transaction_id=transaction_id,
            payment_mode=payment_mode,
            status=status,
            amount=request.amount,
            message=f"{payment_mode} transaction processed with status {status}",
        )

    def get_transaction(self, transaction_id: str) -> Optional[TransactionStatus]:
        return self.transactions.get(transaction_id)

    @staticmethod
    def _validate_payment_mode(payment_mode: str, request: PaymentRequest) -> None:
        if payment_mode == "UPI" and not request.upi_id:
            raise ValueError("UPI ID is required for UPI payments")
        if payment_mode in {"NEFT", "RTGS"} and not request.ifsc_code:
            raise ValueError("IFSC code is required for NEFT/RTGS payments")
