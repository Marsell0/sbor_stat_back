FROM python:3.13

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "sbor_stat/manage.py", "runserver", "0.0.0.0:8000"]