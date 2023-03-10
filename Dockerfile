FROM python:3.9

EXPOSE 8080

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update
RUN apt-get update && apt-get install -y python3-opencv
RUN pip3 install opencv-python-headless==4.5.3.56
sudo yum install mesa-libGL -y
RUN pip install opencv-python

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --no-cache-dir -U install pip

RUN pip install --no-cache-dir install -r requirements.txt

COPY . /app

RUN /bin/sh setup.sh

ENTRYPOINT ["streamlit", "run", "Squat.py"]
