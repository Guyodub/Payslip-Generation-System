# Pull base image
#Docker
FROM python:3.9
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /payslip_generation_project-Master

# Install dependencies
COPY Pipfile Pipfile.lock /payslip_generation_project-Master/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /payslip_generation_project-Master/