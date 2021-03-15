# Pull base image
FROM python:3.8

# Copy files
COPY *.py Pipfile* / 

# Install dependencies
RUN pip install pipenv
RUN pipenv install --system --dev

# Run server
EXPOSE 8000
CMD ["python", "main.py"]
