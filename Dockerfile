FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

EXPOSE 8080

ENV DJANGO_SETTINGS_MODULE=document_processing.settings

ENV DJANGO_SECRET_KEY="django-insecure-963%+cuky9(fp@ajcq&^3ft-@+g7%y)@m-ob)yd8j-wi3u3v^m"

RUN python manage.py collectstatic --noinput

CMD ["bash", "-c", "python manage.py migrate && gunicorn document_processing.wsgi:application --bind 0.0.0.0:8080"]
