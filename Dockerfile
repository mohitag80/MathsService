# Using older Python base image with known OS-level CVEs
FROM python:3.8-bullseye

LABEL maintainer="exam-platform@example.com"
LABEL service="maths-service"
LABEL version="1.0.0"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl gcc libffi-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8082

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV PORT=8082

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
  CMD curl -f http://localhost:8082/health || exit 1

CMD ["python", "app.py"]
