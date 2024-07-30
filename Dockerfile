FROM python:3.9.19-slim-bullseye

RUN mkdir -p /usr/src/cadastro_app

WORKDIR /usr/src/cadastro_app

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
