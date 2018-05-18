FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /bookmarky

WORKDIR /bookmarky

ADD requirements.txt /bookmarky

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

ADD . /bookmarky/
