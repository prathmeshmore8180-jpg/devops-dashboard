# DevOps Service Dashboard (Exp No. 11 Mini-Project)

A complete, lightweight end-to-end DevOps mini-project integrating frontend, backend, automated testing, containerization, orchestration, and continuous integration.

---

## 🛠️ DevOps Tools Used
- **Git & GitHub**: Version control and source code tracking.
- **Docker**: Containerizing the Flask + Gunicorn web service.
- **Docker Compose**: Single-command container deployment and port management.
- **Pytest**: Automated unit testing of endpoints and UI responses.
- **GitHub Actions**: Automated CI/CD pipeline verifying tests and container builds on every commit.

---

## 🚀 Quick Start Instructions

### 1. Run with Docker Compose (Recommended)
Make sure Docker Desktop is running, then run:
```bash
docker compose up --build -d
```
Access the application:
- **Dashboard UI**: [http://localhost:5000](http://localhost:5000)
- **Health Check API**: [http://localhost:5000/health](http://localhost:5000/health)

To stop the container:
```bash
docker compose down
```

---

### 2. Run Locally (Without Docker)
```bash
# Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run automated tests
pytest test_app.py -v

# Start the application
python app.py
```
