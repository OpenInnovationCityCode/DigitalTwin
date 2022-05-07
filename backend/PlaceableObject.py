import numpy as np
class PlaceableObject:

    def __init__(self, long, lat, parameters):
        """Parameters is a dict with a structure { co2: { range : 0, decay : 0, effect : 0} }"""
        self.id = Model.
        # longitude = x, latitude = y -> positions
        self.long = long
        self.lat = lat
        # holds
        self.parameters = parameters





    def get_influence(self, parameter, sensor):
        """Returns float with influence on given coordinate, depending on distance and respective parameter."""
        # TODO: Olis function here

        def difference(sensor_pos, tree_pos, rang, effect, decay):
            dist = np.linalg.norm(np.array(sensor_pos) - np.array(tree_pos))
            return min(effect, ((decay * rang / (dist + 0.0000000001)) * effect)), dist


        sensor_pos = []


