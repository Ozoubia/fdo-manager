FROM python:3.10.5

# forces the output of django to be ou
#ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /fdo_project

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# Copy the Django project code to the container
COPY . .

# Expose the port on which your Django application runs (e.g., 8000)
EXPOSE 8000

# Define the command to run your Django application
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


