sudo docker build . -t img --rm
sudo docker run -it img python -m pytest