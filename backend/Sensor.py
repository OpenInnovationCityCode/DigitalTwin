import random


class Sensor:
    def __init__(self, lat, long, measured_parameters):
        #longitude = x, latitude = y -> positions
        self.long = long
        self.lat = lat
        self.measurements = {parameter : [] for parameter in measured_parameters}
        self.get_timestamp=self.get_timestamp()


    # Dict with values, for every available value e.g. C02, there is a list of time value tuples
    # e.g. {co2: [(14:00, 0.2),(14:01, 0.2)], humidity : [(14:00, 0.3),(14:01, 0.2)]}

    def get_dict_repr(self):
        repr_dict = {"latitude": self.lat, "longitude": self.long,
                     "parameters": dict()}
        for param in self.measurements.keys():
            repr_dict["parameters"][param] = self.measurements[param]
        return repr_dict

    def update_measurements(self):
        """mqtt request stuff here"""
        time=next(self.get_timestamp)
        for parameter in self.measurements.keys():
            self.measurements[parameter].append({"timestamp":time,
                                                 "value":self.get_actual_measurement(parameter)})
        return


    def get_actual_measurement(self, parameter):
        """Get actual measurement for parameter e.g. co2 value"""
        #"co2", "ph", "humidity", "feinstaub", "temp"
        if parameter=="ph":
            return (random.random() - 0.5) * 2 + 7
        if parameter=="humidity":
            return (random.random())
        if parameter=="feinstaub":
            return (random.random())
        if parameter=="co2":
            return (random.random())
        if parameter=="temp":
            return 15
        if parameter=="Lautstärke":
            return 15
        else:
            return random.random()


    def initialize_measurements(self):
        """mqtt request stuff here"""
        time = next(self.get_timestamp)
        for parameter in self.measurements.keys():
            self.measurements[parameter].append({"timestamp": time,
                                                 "value": self.initialize_actual_measurement(parameter)})
        return

    def initialize_actual_measurement(self, parameter):
        """Get actual measurement for parameter e.g. co2 value"""
        # "co2", "ph", "humidity", "feinstaub", "temp"
        if parameter == "ph":
            return (random.random() - 0.5) * 2 + 7
        if parameter == "humidity":
            return (random.random())
        if parameter == "feinstaub":
            return (random.random())
        if parameter == "co2":
            return (random.random())
        if parameter == "temp":
            return 15
        else:
            return random.random()

        #return self.measurements[parameter]+(random.random()-0.5)/4

    def get_timestamp(self):
        for i in range(1000):
            yield i


