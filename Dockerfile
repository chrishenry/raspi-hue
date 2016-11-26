FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir /code/
RUN mkdir /var/lib/raspi-hue/
WORKDIR /code

ADD raspi-hue/ /code/
RUN pip install -r /code/requirements.txt

CMD ["python", "/code/raspi-hue-daemon.py"]
