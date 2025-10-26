
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY requirements.txt .



RUN apt-get update && apt-get install -y gcc pkg-config libmariadb-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*


RUN pip install -r requirements.txt


COPY . .


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
