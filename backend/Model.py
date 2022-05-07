from Sensor import Sensor
import Seb
import random
from PlaceableObject import PlaceableObject

class Model:
    def __init__(self):
        self.sensor_list = []
        self.simulation_sensor_list = []
        # Structur of dicts -> {id : PlaceableObject, id : PlaceableObject2, ...}
        self.placed_objects = dict() #placed at the start
        self.new_placed_objects = dict() #added by us
        self.mapToSend = None
        self.fake_everything(self, 5)

    def get_real_sensors(self):
        return self.sensor_list

    def add_sensor(self, sensor):
        self.sensor_list.append[sensor]

    def add_placeable_object(self, name, long, lat, parameters):
        """Adds placed object"""
        pl_obj = PlaceableObject(name, long, lat, parameters)
        self.placed_objects[pl_obj.id] = pl_obj

    def add_new_placeable_object(self, name, long, lat, parameters):
        """Adds new placed object"""
        pl_obj = PlaceableObject(name, long, lat, parameters)
        self.new_placed_objects[pl_obj.id] = pl_obj


    def delete_object_from_placed_objects(self, placeableObjectID):
        """Add specified object to -> unterscheiden -> new placed auch!"""


    def get_current_results(self):
        """Format as in api/results.json. Interpolates data with used resolution
        Everything ready for view except jsonify. Gives map to stuff"""
        results = dict()
        results["data"] = {"objects": {"placed": [], "new_placed": [], "deleted": []},
                           "measurements": []}
        # add placed objects
        for object in self.placed_objects:
            dict_repr = object.get_dict_repr()
            if dict_repr["deleted"]:
                results["data"]["objects"]["deleted"].append(dict_repr)
            else:
                results["data"]["objects"]["placed"].append(dict_repr)
        # add placed objects
        for object in self.new_placed_objects:
            dict_repr = object.get_dict_repr()
            if dict_repr["deleted"]:
                results["data"]["objects"]["deleted"].append(dict_repr)
            else:
                results["data"]["objects"]["new_placed"].append(dict_repr)
        # add measurements
        for
        results["data"]["measurements"]



    def fake_everything(self,nr):
        end=False
        while end==False:
            try:
                self.mapToSend, Park_area = Seb.get_Park()
                area_range = Seb.get_max_square(Park_area)
                end=True
            except:
                pass
        Places=Seb.get_Messgerät(nr,self.mapToSend, area_range) #returns list of long,lat in the garden

        for new_sensor in range(nr):
            self.sensor_list.append(Sensor(Places[new_sensor][0],Places[new_sensor][1],[random.random(),(random.random()-0.5)*2+7]))
