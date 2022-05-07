import numpy as np
import Model as Model

class PlaceableObject:
    def __init__(self, long, lat, parameters):
        """Parameters is a dict with a structure { co2: { range : 0, decay : 0, effect : 0} }"""
        Model.placeable_objects_count += 1
        self.id = Model.placeable_objects_count
        # longitude = x, latitude = y -> positions
        self.long = long
        self.lat = lat
        # holds
        self.parameters = parameters


    def get_influence_difference(self, parameter, sensor, negate = False):
        """Returns float with influence on given coordinate, depending on distance and respective parameter."""
        # TODO: Olis function here
        sensor_pos = [sensor.long, sensor.lat]
        tree_pos = [self.long, self.lat]
        range = self.parameters[parameter]["range"]
        effect = self.parameters[parameter]["effect"]
        decay = self.parameters[parameter]["decay"]
        dist = np.linalg.norm(np.array(sensor_pos) - np.array(tree_pos))
        difference = min(effect, ((decay * range / (dist + 0.0000000001)) * effect))
        if negate:
            difference = -difference
        return difference, dist




