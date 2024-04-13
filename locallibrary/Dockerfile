FROM python:3.11
LABEL maintainer="Veysel Aksin"

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

COPY . /app
WORKDIR /app

EXPOSE 8000

RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
