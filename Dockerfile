#Download Python
FROM python:3.7.4

#Set working directory
WORKDIR /code

#Copy the dependencies to the work dir
COPY requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy Flask app to the work dir
COPY src/ .

#Run the container
CMD ["python", "./app.py"]