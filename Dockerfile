FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY knn.py .

# Define the command to run your Flask app
# CMD ["python", "knn.py"]
