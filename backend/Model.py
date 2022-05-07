from backend.Sensor import Sensor
import Seb
import random




class Model:

    def __init__(self):
        self.placeable_objects_count = 0
        self.sensor_list = []
        self.simulation_sensor_list = []
        # Structur of dicts -> {id : PlaceableObject, id : PlaceableObject2, ...}
        self.placed_objects = dict() #placed at the start
        self.new_placed_objects = dict() #added by us
        self.deleted_objects = dict() #deleted placed and new placed
        self.mapToSend = None

    def get_real_sensors(self):
        return self.sensor_list

    def add_sensor(self, sensor):
        self.sensor_list.append[sensor]

    def add_placeable_object(self, placeableObject):
        """Adds new placed object"""
        self.placed_objects

    def delete_object_from_placed_objects(self, placeableObjectID):
        """Add specified object to """

    def delete_object_from_placed_objects(self, placeableObjectID):
        """"""

    def get_current_results(self):
        """Format as in api/results.json. Interpolates data with used resolution"""


    def fake_everything(self,nr):
        end=False
        while end=False:
            try:
                self.mapToSend, Park_area = Seb.get_Park()
                area_range = Seb.get_max_square(Park_area)
                end=True
            except:
                pass
        Places=Seb.get_Messgerät(nr,self.mapToSend, area_range) #returns list of long,lat in the garden

        for new_sensor in range(nr):
            self.sensor_list.append(Sensor(Places[new_sensor][0],Places[new_sensor][1],[random.random(),(random.random()-0.5)*2+7]))



tesst = Model()
tesst.fake_everything(6)
print(tesst.sensor_list)