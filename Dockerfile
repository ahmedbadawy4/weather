FROM python:3.6-slim-stretch
ARG API_KEY
ENV API_KEY=$API_KEY
RUN pip install -U pip
RUN pip install pipenv
COPY app.py .
COPY weather.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]
