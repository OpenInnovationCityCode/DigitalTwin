import argparse
import logging
import textwrap
from pathlib import Path
import json

from flask import Flask, jsonify, request

app = Flask(__name__)


mockup = {
  "data": {
    "objects": {
      "placed": [
        {
          "id": 1,
          "name": "tree",
          "latitude": 51.3356,
          "longitude": 8.246252
        },
        {
          "id": 2,
          "name": "tree",
          "latitude": 51.3356,
          "longitude": 8.246252
        },
        {
          "id": 3,
          "name": "tree",
          "latitude": 51.3356,
          "longitude": 8.24625
        }
      ],
      "new_placed": [],
      "deleted": []
    },
    "measurements": [
      {
        "latitude": 51.3356,
        "longitude": 8.246252,
        "parameters": {
          "co2": [
            {
              "timestamp": 1651927953843,
              "value": 0.621
            },
            {
              "timestamp": 1651927958843,
              "value": 0.621
            }
          ],
          "ph": [
            {
              "timestamp": 1651927953843,
              "value": 0.621
            },
            {
              "timestamp": 1651927958843,
              "value": 0.621
            }
          ]
        }
      },
      {
        "latitude": 51.3356,
        "longitude": 8.246252,
        "parameters": {
          "co2": [
            {
              "timestamp": 1651927953843,
              "value": 0.621
            },
            {
              "timestamp": 1651927958843,
              "value": 0.621
            }
          ],
          "ph": [
            {
              "timestamp": 1651927953843,
              "value": 0.621
            },
            {
              "timestamp": 1651927958843,
              "value": 0.621
            }
          ]
        }
      }
    ]
  }
}


OBJECT_DEFINITIONS ={'tree': {"CO2":{'range':4,'decay':1,'effect':0.5},"PH":{'range':4,'decay':1,'effect':4}},
                     'hedge': {"CO2":{'range':4,'decay':1,'effect':0.2},"PH":{'range':4,'decay':1,'effect':1.5}}}



@app.route("/api/get_world",methods =['GET'])
def get_world():
    """
    bodyless request, gets current simulated world state.


    :return: see api/
    """
    # TODO return simulated state from model


    return mockup


@app.route("/api/delete/",methods =['POST'])
def delete():
    # get data from request
    data = request.get_json()

    id = data['id']


    # todo: model.delete(id)

    # TODO return simulated state from model
    return mockup

@app.route("/api/place/",methods =['POST'])
def place():


    # get data from request
    data = request.get_json()

    # find definition
    found = False

    for object_name in OBJECT_DEFINITIONS.keys():
        if data['name'] == object_name:
          found = True
          definition = OBJECT_DEFINITIONS[object_name]

    # use dfault tree if not found
    if not found :
      definition = OBJECT_DEFINITIONS['tree']

    # todo: model.place(data['long'],data['lat'], definition)

    # TODO return simulated state from model
    return mockup




    return mockup

if __name__ == '__main__':
    # TODO: init model!
    #model=new_model()

    app.run(port=5000, debug=True)
