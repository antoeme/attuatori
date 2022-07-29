FROM python:3.9.13-alpine3.15

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "flask", "run" ]