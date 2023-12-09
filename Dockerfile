# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the built wheel file from your host to the container
COPY ./dist/Volun2k9App-0.1.0-py3-none-any.whl .

# Install the Flask app from the wheel file
RUN pip install Volun2k9App-0.1.0-py3-none-any.whl

# Your Flask application's default port
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
