FROM python:3.6-slim-stretch
RUN pip install -U pip
RUN pip install pipenv
COPY app.py .
COPY weather.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]
