FROM python:3.9-alpine
LABEL maintainer="Lainnyone"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./portfolio /app

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django

ENV PATH="/py/bin:$PATH"

USER django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
