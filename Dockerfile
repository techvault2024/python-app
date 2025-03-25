FROM python:3.12-slim
COPY ./src /app
COPY requirements.txt /app
WORKDIR /app
RUN python3 -m venv /app/venv \
    && . /app/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
CMD ["/app/venv/bin/python", "app.py"]