#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from task import task
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    task.start_backend_schedule()
    app.run()
