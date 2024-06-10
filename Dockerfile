FROM python:3.9-slim

WORKDIR /App

COPY requirements.txt /App/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /App

EXPOSE 5500
ENV FLASK_APP=App.py
CMD ["flask", "run", "--host=127.0.0.1"]






