FROM python:alpine3.7
COPY . /pythondockerapp
WORKDIR /pythondockerapp
RUN pip install flask
EXPOSE 5000
CMD python ./helloworld.py