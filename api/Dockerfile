FROM python:3.11-slim


WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY app/ /app

CMD ["python", "flask_app.py"]