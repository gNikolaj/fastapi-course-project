# FastAPI Course Project

## Project Structure

```text
fastapi-course-project/
├── backend/    # FastAPI application
└── frontend/   # React application
```

## Backend

### Requirements

- Python 3.9+
- pip

### Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
make run
```

or

```bash
uvicorn main:app --reload
```

### Tests

```bash
make test
```

or

```bash
pytest
```

### Environment Variables

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env
```

## Docker

### Requirements

- Docker Desktop

### Build

```bash
cd backend
docker build -t fastapi-app .
```

### Run

```bash
docker run -p 8000:8000 fastapi-app
```

or

```bash
make docker-build
make docker-run
```

## Database Migrations

### Requirements

- PostgreSQL running locally or via Docker

### Initialize migrations (already done)

```bash
alembic init migrations
```

### Create a new migration

```bash
alembic revision --autogenerate -m "description"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback last migration

```bash
alembic downgrade -1
```

### Check current migration version

```bash
alembic current
```

## Frontend

### Requirements

- Node.js
- npm

### Setup

```bash
cd frontend
npm install
```

### Run

```bash
npm run dev
```