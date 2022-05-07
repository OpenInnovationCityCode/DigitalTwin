import argparse
import logging
import textwrap
from pathlib import Path
import json

from flask import Flask, jsonify, request

app = Flask(__name__)


def new_model():
    return {'test1': 'bla',
            'test2': 'bli',
            'test3': 'blub'}


@app.route("/api/hello_world")
def hello_world():
    load = jsonify({'is_alive': model['test1']})
    return load


@app.route("/api/hello")
def hello_world_j():
    load = jsonify({'is_alive': True,
                    'hoehe': 1.6,
                    'x': 50003485.32432,
                    'y': 3249843.123,
                    })
    return load

@app.route("/api/trees")
def trees():
    load = jsonify({'is_alive': True,
                    'hoehe': 1.6,
                    'x': 50003485.32432,
                    'y': 3249843.123,
                    })
    return load


if __name__ == '__main__':
    model=new_model()
    app.run(port=5000, debug=True)
