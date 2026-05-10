# MathsService

Microservice for Mathematics exam questions for Grade 9-12 students. Part of the **ExamPlatform** suite.

## Tech Stack

- **Language**: Python 3.8
- **Framework**: Flask 1.1.2
- **Build Tool**: pip
- **Container**: Docker

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/maths/questions/grade/{grade}/top/{n}` | Top N questions for a grade |
| GET | `/api/maths/questions/topic/{topic}/count/{n}` | N questions by topic |
| GET | `/api/maths/questions/complexity/{complexity}/count/{n}` | N questions by complexity |
| GET | `/api/maths/questions/grade/{grade}/topic/{topic}/count/{n}` | N questions by grade + topic |
| GET | `/api/maths/topics` | List all available topics |
| GET | `/api/maths/stats` | Question bank statistics |

## Supported Topics

- Algebra
- Geometry
- Coordinate Geometry
- Statistics
- Calculus
- Trigonometry
- Matrices
- Probability
- Vectors

## Complexity Levels

- `easy` — 1 mark
- `medium` — 2 marks
- `hard` — 3 marks

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

Service starts on port **8082**.

### Example Requests

```bash
# Top 5 questions for Grade 11
curl http://localhost:8082/api/maths/questions/grade/11/top/5

# 4 Calculus questions
curl http://localhost:8082/api/maths/questions/topic/Calculus/count/4

# 3 hard questions
curl http://localhost:8082/api/maths/questions/complexity/hard/count/3
```

## Docker

```bash
docker build -t maths-service:1.0.0 .
docker run -p 8082:8082 maths-service:1.0.0
```
