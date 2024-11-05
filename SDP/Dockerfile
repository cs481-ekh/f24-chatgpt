#uses a lightweight python image
FROM python:3.10-slim

#ensures that the python output is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED = 1

# sets the working directory to /SDP
WORKDIR /SDP

#copies the current directory contents into the container at /SDP
COPY requirements.txt /SDP/requirements.txt

#installs any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#copies the current directory contents into the container at /app
COPY . /SDP

#makes port 8000 available to the world outside this container
EXPOSE 8000

#runs manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#http://localhost:8000/ to access the application