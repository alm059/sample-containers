FROM python:3.12.2-bookworm

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN rm requirements.txt

COPY ./app/ .

EXPOSE 8080/tcp

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]