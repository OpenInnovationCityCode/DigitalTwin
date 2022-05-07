class Model:

    def __init__(self):
        self.sensor_list = []
        self.simulation_sensor_list = []
        # Structure -> id : PlaceableObject

        self.placed_objects = dict() #placed at the start
        self.new_placed_objects = dict() #added by us
        self.deleted_objects = dict() #deleted placed and new placed

    def get_real_sensors(self):
        return self.sensor_list

    def add_sensor(self, sensor):
        self.sensor_list.append[sensor]

    def add_placeable_object(self, placeableObject):
        """Adds new placed object"""
        self.placed_objects

    def delete_object_from_placed_objects(self, placeableObjectID):
        """Add specified object to """

    def delete_object_from_placed_objects(self, placeableObject):
        """"""

    def get_current_results(self):
        """Format as in api/results.json. Interpolates data with used resolution"""




