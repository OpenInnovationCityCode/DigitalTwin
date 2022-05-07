import random


class Sensor:
    def __init__(self, lat, long, measured_parameters):
        #longitude = x, latitude = y -> positions
        self.long = long
        self.lat = lat
        self.measurements = {parameter : [] for parameter in measured_parameters}


    # Dict with values, for every available value e.g. C02, there is a list of time value tuples
    # e.g. {co2: [(14:00, 0.2),(14:01, 0.2)], humidity : [(14:00, 0.3),(14:01, 0.2)]}

    def update_measurements(self):
        """mqtt request stuff here"""
        for parameter in measurements.keys():
            self.measurements[parameter].append((self.get_timestamp(),
                                                 self.get_actual_measurement(parameter)))


    def get_actual_measurement(self, parameter):
        """Get actual measurement for parameter e.g. co2 value"""
        return self.measurements[parameter]+(random.random()-0.5)/4

        pass

    def get_timestamp(self):

        pass

    def update_with_fake_measurements(self):
        pass