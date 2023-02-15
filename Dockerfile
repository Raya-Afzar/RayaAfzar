# Pull base image
FROM python:3.8
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /home/farsad/Files/Projects/mysite_project/

# Install dependencies
COPY Pipfile Pipfile.lock /home/farsad/Files/Projects/mysite_project/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /home/farsad/Files/Projects/mysite_project/
