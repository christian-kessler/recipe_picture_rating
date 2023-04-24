import platform
import os
import json

from flask import Flask, request

from app import app
from env.config_parser import config, GATEWAY_HOST, DO_REGISTRATION, GATEWAY_URL, REGISTRY_URL, MY_NAME, MY_PORT
from app.registry import registry_client
from app.service import ImageService

service = ImageService()


@app.route("/deku/api/v1/image")
def index():
    url = request.args.get('url')
    return {"payload": str(service.predict(url))}


@app.route("/train")
def train():
    service.train()
    return "Done"


def run():
    gateway_host = config[GATEWAY_HOST]
    gateway_url = config[GATEWAY_URL]
    registry_url = config[REGISTRY_URL]
    do_registration = config[DO_REGISTRATION]
    my_name = config[MY_NAME]
    my_port = config[MY_PORT]

    registry_client.register(
        registry_url,
        my_port,
        my_name,
        do_registration,
    )

    app.run(host='0.0.0.0', port=my_port, threaded=False)
