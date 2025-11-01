# Use the official Python runtime image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . /app/

# Expose Django port
EXPOSE 8006

# Compile messages for all supported languages
# Add all languages from your LANGUAGES list
RUN python manage.py makemessages -l en || true
RUN python manage.py makemessages -l tr || true
RUN python manage.py makemessages -l ms || true
RUN python.manage.py makemessages -l ko || true
RUN python.manage.py makemessages -l ru || true
RUN python.manage.py makemessages -l es || true
RUN python.manage.py makemessages -l zh-hans || true
RUN python.manage.py makemessages -l ar || true

RUN python manage.py compilemessages

# Run migrations
RUN python manage.py migrate

# Default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8006"]
