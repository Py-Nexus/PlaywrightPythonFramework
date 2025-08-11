#FROM python:3.13-slim
# Uncomment the above line if you want to use a specific Python version

# Use the Playwright Python image as the base image
FROM mcr.microsoft.com/playwright/python:v1.54.0-noble

# Set the environment variable to avoid warnings about pip running as root
ENV PIP_ROOT_USER_ACTION=ignore

# Set the working directory in the container
WORKDIR /app
ENV PYTHONPATH=/app
# Copy the necessary files into the container
COPY pages /app/pages
COPY testcases /app/testcases
COPY utilities /app/utilities
COPY configdata /app/configdata
COPY .gitignore /app/
COPY Dockerfile /app/
COPY pytest.ini /app/
COPY README.md /app/
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir --upgrade pip setuptools \
  && pip install --no-cache-dir -r requirements.txt

# Set the default command to run tests
CMD ["pytest", "--reportportal"]