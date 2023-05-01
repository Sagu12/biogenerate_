# FROM python:3.9-slim-buster

FROM nvidia/cuda:11.6.2-base-ubuntu20.04

ENV TZ=Asia/Dubai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt install -y tzdata

# Set the working directory to /code
WORKDIR /code

# copy the requirements file used for dependencies
COPY src/prediction /code/src/prediction

RUN apt-get update

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "src.prediction.main:app", "--host", "0.0.0.0", "--port", "80"]