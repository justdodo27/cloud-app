# backend/Dockerfile
FROM python:3.11

# Load backend app
WORKDIR /app

COPY ./app .
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Load data
WORKDIR /data
COPY ./data .

# Install netcat
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

WORKDIR /
COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh
WORKDIR /app

ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
