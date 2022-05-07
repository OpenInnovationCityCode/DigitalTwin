import numpy as np

class PlaceableObject:
    placeable_objects_count = 0
    def __init__(self, name, long, lat, parameters):
        """Parameters is a dict with a structure { co2: { range : 0, decay : 0, effect : 0} }"""
        self.placeable_objects_count += 1
        self.id = self.placeable_objects_count
        self.name = name
        # longitude = x, latitude = y -> positions
        self.long = long
        self.lat = lat
        # holds
        self.parameters = parameters
        self.deleted = False

    def get_dict_repr(self):
        return {"id": self.id,
                "name": self.name,
                "latitude": self.lat,
                "longitude": self.long,
                "deleted": self.deleted}

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




