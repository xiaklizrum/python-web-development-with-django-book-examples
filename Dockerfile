FROM python:3.8.0
WORKDIR /tmp
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt