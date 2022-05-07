import argparse
import logging
import textwrap
from pathlib import Path
import json
from Model import Model

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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


global model
OBJECT_DEFINITIONS ={'tree': {"CO2":{'range':4,'decay':1,'effect':0.5},"PH":{'range':4,'decay':1,'effect':4}},
                     'hedge': {"CO2":{'range':4,'decay':1,'effect':0.2},"PH":{'range':4,'decay':1,'effect':1.5}}}



@app.route("/api/get_world",methods =['GET'])
@cross_origin()
def get_world():
    """
    gets current simulated world state,bodyless request


    :return: see api/
    """

    global model


    return model.get_current_results()


@app.route("/api/delete/",methods =['POST'])
@cross_origin()
def delete():

    """
    Deletes object by id. expects body of form {'id':12}
    """
    # get data from request
    global model
    data = request.get_json()

    id = data['id']


    model.delete_object_from_placed_objects(id)

    return model.get_current_results()

@app.route("/api/place/",methods =['POST'])
@cross_origin()
def place():
    """
    Places new object in model. expects body of form
    {'name':'tree','long':49,'lat':31}
    """

    global model
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

    model.add_placeable_object(data['name'], data['long'],data['lat'], definition)

    return model.get_current_results()





if __name__ == '__main__':

    global model
    model = Model()

    app.run(port=5000, debug=True)

