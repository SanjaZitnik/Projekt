FROM python:3.8
RUN python3 -m pip install flask pony
RUN mkdir /app
WORKDIR /app
COPY app.py /app/
COPY requirements.txt /app/
COPY Templates /app/Templates  
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 5500
CMD ["flask", "run", "--host=0.0.0.0", "--port=5500"]






