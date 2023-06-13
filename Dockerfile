FROM python:3.9

# Setting environment variables. (Good Practice)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install django Pillow

# Copy the django project
COPY . /app/

# Set the current working directory
WORKDIR /app

# Expose the necessary port for action
EXPOSE 8000

# Set the start up command
CMD [ "python3", "/app/babyshop_app/manage.py", "runserver", "0.0.0.0:8000"]