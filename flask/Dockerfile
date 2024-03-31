# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /flask
WORKDIR /flask

# Copy the current directory contents into the container at /app
COPY . /flask

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK_ENV=production
ENV FLASK_APP=main.py

# Run Gunicorn when the container launches
#CMD ["gunicorn", "-b", "0.0.0.0:80", "wsgi:application"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
