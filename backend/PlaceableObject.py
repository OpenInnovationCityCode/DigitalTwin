class PlaceableObject:
    def __init__(self, long, lat, parameters, ids, ranges, decays, effects):
        # longitude = x, latitude = y -> positions
        self.long = long
        self.lat = lat
        # holds
        self.parameter_dict = { par : dict() for par in parameters}
        for key in self.influence_on_sensors_parameters_dict.keys():



    def get_influence(self, parameter, sensor):
        """Returns float with influence on given coordinate, depending on distance and respective parameter."""
        # TODO: Olis function here