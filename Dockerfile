# set base image (host OS)
FROM python:3.8


#required for textract
RUN apt-get update && apt-get install -y \ 
python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig

# install dependencies
RUN python -m pip install pip-tools

# set the working directory in the container
WORKDIR /code
RUN mkdir "tests"

# copy the dependencies file to the working directory
COPY requirements.in /code

RUN pip-compile

# install dependencies
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

COPY src/ /code
COPY main.py /code
COPY tests/ /code/tests/
COPY data/ /code/data

# command to run on container start
CMD [ "python","-u",  "./main.py" ] 