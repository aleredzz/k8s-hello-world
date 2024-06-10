#!/bin/python
from flask import Flask, request, make_response
import os

app = Flask(__name__)


@app.route("/")
def router():
    route_to_hello = request.cookies.get("route_to_hello")
    if route_to_hello is None or route_to_hello == "true":
        return hello()
    else:
        return world()


def hello():
    response = make_response(f"<h1> {os.getenv('HELLO_VALUE')}... </h1>")
    response.set_cookie("route_to_hello", "false")
    return response


def world():
    response = make_response(f"<h1> ... {os.getenv('WORLD_VALUE')}! </h1>")
    response.set_cookie("route_to_hello", "true")
    return response
