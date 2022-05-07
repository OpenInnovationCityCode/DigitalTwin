class Sensor:
    # Dict with values, for every available value e.g. C02, there is a list of time value tuples
    measurements = dict();

    def __init__(self, parameters):
        for 