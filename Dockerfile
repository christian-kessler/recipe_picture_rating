FROM ubuntu:16.04

#RUN add-apt-repository ppa:jonathonf/python-3.6

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip libglib2.0-0 libsm6 libxext6 libxrender1 libfontconfig1

RUN pip3 install pipenv
RUN pip3 install tensorflow


ENV DEKU_ENV=production \
    GOOS=linux \
    GOARCH=amd64 \
    CGO_ENABLED=0 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /app

# COPY ./deku /app
COPY . /app

RUN pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT [ "python3" ]

CMD [ "deku/main.py" ]

