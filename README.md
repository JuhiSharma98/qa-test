# qa-test
# QA Test Automation

## Setup and Run

### Prerequisites
- Minikube or Kind
- kubectl
- Python 3.x
- pytest
- requests

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Vengatesh-m/qa-test.git
    cd qa-test
    ```

2. **Start Minikube or Kind**:
    ```sh
    minikube start
    # OR for Kind
    kind create cluster
    ```

3. **Deploy the services**:
    ```sh
    kubectl apply -f backend/deployment.yaml
    kubectl apply -f frontend/deployment.yaml
    ```

4. **Get the frontend URL**:
    ```sh
    minikube service frontend-service --url
    ```

5. **Run the automated test**:
    ```sh
    pip install pytest requests
    pytest test_integration.py
    ```

## Test Script

The test script `test_integration.py` verifies the integration between the frontend and backend services.
