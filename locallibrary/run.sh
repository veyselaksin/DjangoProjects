#!/bin/sh

docker build -t locallibrary .

docker run -p 8000:8000 --env-file .env -v $(pwd):/app locallibrary
