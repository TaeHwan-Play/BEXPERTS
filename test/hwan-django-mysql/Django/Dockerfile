FROM python:3.8.6
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install mysqlclient && pip install -r requirements.txt
COPY . /code/