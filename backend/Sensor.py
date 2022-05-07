class Sensor:
    def __init__(self, lat, long, measured_parameters):
        #longitude = x, latitude = y -> positions
        self.long = long
        self.lat = lat
        self.measurements = {parameter : [] for parameter in measured_parameters}


    # Dict with values, for every available value e.g. C02, there is a list of time value tuples

    def update_measurements(self):
        """mqtt request stuff here"""
        for parameter in measurements.keys():
            measurements[parameter].append()


    def get_actual_measurement(self, parameter):
        """Get actual measurement for parameter e.g. co2 value"""
        pass

    def get_timestamp(self):

        pass