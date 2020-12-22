# set base image (host OS)
FROM python:3.8

# install dependencies
RUN python -m pip install pip-tools

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.in /code

RUN pip-compile

# install dependencies
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

COPY src/ /code
COPY main.py /code

# command to run on container start
CMD [ "python","-u",  "./main.py" ] 