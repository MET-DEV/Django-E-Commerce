FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /usr/code
WORKDIR /usr/code/babyshop_app
RUN pip3 install -r /usr/code/requirements.txt &&\
    python3 manage.py migrate

ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]