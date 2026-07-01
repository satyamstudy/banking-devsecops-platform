# Runbook

## Local Service Check

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ready
curl http://localhost:8000/metrics
```

## Create UPI Transaction

```bash
curl -X POST http://localhost:8000/api/v1/payments/upi \
  -H "Content-Type: application/json" \
  -d '{"customer_id":"CUST1001","beneficiary_account":"1234567890","upi_id":"satyam@upi","amount":5000,"remarks":"UPI payment"}'
```

## Kubernetes Checks

```bash
kubectl get pods -n banking-devsecops
kubectl get svc -n banking-devsecops
kubectl logs -n banking-devsecops deploy/banking-devsecops-api
kubectl describe pod -n banking-devsecops -l app=banking-devsecops-api
```

## Common Issues

| Issue | Check |
|---|---|
| Pod not starting | Check image name, imagePullPolicy, resource limits |
| Readiness failing | Check `/ready` endpoint and container port |
| Service not reachable | Check selector labels and targetPort |
| CI failing | Check requirements, tests, Python version, scanner logs |
