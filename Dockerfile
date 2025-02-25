FROM python:latest
WORKDIR /app
RUN apt-get update

COPY requirments.txt .
RUN pip install -r requirments.txt

COPY . .

CMD ["pytest", "tests/"]