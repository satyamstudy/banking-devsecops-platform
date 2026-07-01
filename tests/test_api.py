from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_upi_payment():
    payload = {
        "customer_id": "CUST1001",
        "beneficiary_account": "1234567890",
        "upi_id": "satyam@upi",
        "amount": 5000,
        "remarks": "UPI test payment",
    }
    response = client.post("/api/v1/payments/upi", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["payment_mode"] == "UPI"
    assert body["status"] == "SUCCESS"


def test_create_neft_payment():
    payload = {
        "customer_id": "CUST1002",
        "beneficiary_account": "9876543210",
        "ifsc_code": "HDFC0001234",
        "amount": 75000,
        "remarks": "NEFT vendor payment",
    }
    response = client.post("/api/v1/payments/neft", json=payload)
    assert response.status_code == 200
    assert response.json()["payment_mode"] == "NEFT"


def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "banking_api_requests_total" in response.text
