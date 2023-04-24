import threading
import requests
import json
import os
import socket
import logging

registryUrl = None
myPort = None
myName = None
doRegistration = None
myUrl = None


def set_vars(regUrl, port, name, doIt):
    global registryUrl
    global myPort
    global myName
    global doRegistration
    global myUrl

    registryUrl = regUrl
    myPort = str(port)
    myName = name
    doRegistration = doIt

    if "DOCKER_HOST" in os.environ:
        myUrl = os.environ['DOCKER_HOST']

    if myUrl is None:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        myUrl = 'http://' + s.getsockname()[0]
        s.close()
    else:
        myUrl = "http://" + myUrl


def register(regUrl, port, name, doIt):

    set_vars(regUrl, port, name, doIt)

    if doRegistration == 'True':
        registerService()
        sendPingPeriodically()


def registerService():
    url = registryUrl + "/registry/api/v1/register"

    sendServiceData(url)


def sendPingPeriodically():
    threading.Timer(10.0, sendPingPeriodically).start()
    pingRegistry()


def pingRegistry():
    url = registryUrl + "/registry/api/v1/ping"

    sendServiceData(url)


def sendServiceData(url):
    data = {
        'name': myName,
        'port': myPort,
        'url': myUrl
    }
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain', "Connection": "close"}

    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    logging.debug('Status of request: %s for url %s', r.status_code, url)

    if r.status_code == 404:
        registerService()
