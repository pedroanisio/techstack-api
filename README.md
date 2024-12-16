# TechStack API

## Overview
TechStack API is a FastAPI-based application designed to manage a catalog of technology stacks and their versions. It provides endpoints to create, retrieve, and update tech stacks and their respective versions. The API supports SQLite as its default database.

---

## Features
- **Health Check**: Ensures the service is operational.
- **CRUD Operations**:
  - Retrieve all tech stacks.
  - Retrieve a tech stack by name.
  - Retrieve all versions of a tech stack.
  - Create a new tech stack with optional versions.
  - Add new versions to an existing tech stack.
- **SQLAlchemy ORM** for database interaction.
- **Pydantic Models** for request validation and response serialization.

---

## Folder Structure
```
techstack_api/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app entry point
│   ├── models.py       # SQLAlchemy ORM models
│   ├── schemas.py      # Pydantic models for request/response validation
│   ├── database.py     # Database configuration and connection
│   ├── routes.py       # API route definitions
│   └── dependencies.py # Shared dependencies (e.g., database session)
├── tests/
│   ├── __init__.py
│   └── test_routes.py  # Test cases for API routes
├── requirements.txt    # Python dependencies
├── Dockerfile          # Containerize the application
└── docker-compose.yml  # Docker Compose configuration
```

---

## Requirements
- Python 3.10+
- SQLite
- pip

---

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd techstack_api
```

### 2. Create a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn app.main:app --reload
```
Access the application at `http://127.0.0.1:8000`.

---

## Running with Docker

### 1. Build the Docker Image
```bash
docker build -t techstack-api .
```

### 2. Run the Container
```bash
docker-compose up
```
Access the application at `http://127.0.0.1:8000`.

---

## API Endpoints

### Health Check
- **GET** `/health`
  - Response: `{ "status": "ok" }`

### Tech Stack Management

#### Get All Tech Stacks
- **GET** `/techstack`
  - Response: List of all tech stacks.

#### Get Tech Stack by Name
- **GET** `/techstack/{name}`
  - Path Parameter: `name` (string)
  - Response: Details of the tech stack.

#### Get Tech Stack Versions
- **GET** `/techstack/{name}/versions`
  - Path Parameter: `name` (string)
  - Response: List of versions for the tech stack.

#### Create Tech Stack
- **POST** `/techstack`
  - Request Body: Tech stack details and optional versions.
  - Response: Created tech stack.

#### Add Version to Tech Stack
- **POST** `/techstack/{name}/versions`
  - Path Parameter: `name` (string)
  - Request Body: Version details.
  - Response: Created version.

---

## Testing

### Install Testing Dependencies
```bash
pip install pytest
```

### Run Tests
```bash
pytest tests/
```

---

## Deployment

### Steps
1. **Build and Push Docker Image**:
   ```bash
   docker build -t <registry>/techstack-api:latest .
   docker push <registry>/techstack-api:latest
   ```
2. **Deploy with Docker Compose**:
   - Update `docker-compose.yml` to pull the image from your container registry.
   - Run `docker-compose up` on the server.

### Monitoring
- **Health Checks**: Use `/health` endpoint for readiness probes.
- **Logging**: Ensure logs are collected and analyzed using tools like ELK stack.
- **Telemetry**: Integrate Prometheus for metrics collection.

---

## Future Improvements
- Add authentication and authorization.
- Implement pagination for large datasets.
- Migrate to a more robust database (e.g., PostgreSQL).
- Integrate Swagger documentation at `/docs`.

---

## Contributing
1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request with detailed comments.

---

## License
This project is licensed under the MIT License.

