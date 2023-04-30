FROM python:3.9-slim-buster

# Set the working directory to /code
WORKDIR /code

# copy the requirements file used for dependencies
COPY src/prediction /code/src/prediction

RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get install git-lfs

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "src.prediction.main:app", "--host", "0.0.0.0", "--port", "80"]