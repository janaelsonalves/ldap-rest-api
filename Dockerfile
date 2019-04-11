FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy

EXPOSE 80

CMD ["gunicorn" "-b", "0.0.0.0:80", "wsgi:app"]