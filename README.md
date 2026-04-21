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