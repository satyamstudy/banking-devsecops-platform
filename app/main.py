from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

from app.models import PaymentRequest, PaymentResponse, TransactionStatus
from app.services.payment_service import PaymentService

app = FastAPI(
    title="Banking DevSecOps Payment API",
    description="Mock banking payment service for UPI, NEFT, RTGS and NPCI-style transaction workflows.",
    version="1.0.0",
)

payment_service = PaymentService()

REQUEST_COUNT = Counter(
    "banking_api_requests_total",
    "Total number of API requests",
    ["method", "endpoint"],
)
REQUEST_LATENCY = Histogram(
    "banking_api_request_latency_seconds",
    "API request latency in seconds",
    ["endpoint"],
)


@app.get("/health")
def health():
    REQUEST_COUNT.labels(method="GET", endpoint="/health").inc()
    return {"status": "healthy", "service": "banking-devsecops-api"}


@app.get("/ready")
def ready():
    REQUEST_COUNT.labels(method="GET", endpoint="/ready").inc()
    return {"status": "ready", "dependencies": {"database": "mock", "registry": "mock"}}


@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/api/v1/payments/upi", response_model=PaymentResponse)
def create_upi_payment(request: PaymentRequest):
    REQUEST_COUNT.labels(method="POST", endpoint="/api/v1/payments/upi").inc()
    with REQUEST_LATENCY.labels(endpoint="/api/v1/payments/upi").time():
        return payment_service.create_payment("UPI", request)


@app.post("/api/v1/payments/neft", response_model=PaymentResponse)
def create_neft_payment(request: PaymentRequest):
    REQUEST_COUNT.labels(method="POST", endpoint="/api/v1/payments/neft").inc()
    with REQUEST_LATENCY.labels(endpoint="/api/v1/payments/neft").time():
        return payment_service.create_payment("NEFT", request)


@app.post("/api/v1/payments/rtgs", response_model=PaymentResponse)
def create_rtgs_payment(request: PaymentRequest):
    REQUEST_COUNT.labels(method="POST", endpoint="/api/v1/payments/rtgs").inc()
    with REQUEST_LATENCY.labels(endpoint="/api/v1/payments/rtgs").time():
        return payment_service.create_payment("RTGS", request)


@app.get("/api/v1/transactions/{transaction_id}", response_model=TransactionStatus)
def get_transaction(transaction_id: str):
    REQUEST_COUNT.labels(method="GET", endpoint="/api/v1/transactions/{transaction_id}").inc()
    transaction = payment_service.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
