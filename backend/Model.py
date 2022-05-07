from Sensor import Sensor
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
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
        self.fake_everything()

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
        """Format as in api/results.json.
        Everything ready for view except jsonify. Gives map to stuff"""
        results = dict()
        results["data"] = {"objects": {"placed": [], "new_placed": [], "deleted": []},
                           "measurements": []}
        # add placed objects
        for _ , pl_obj in self.placed_objects.items():
            dict_repr = pl_obj.get_dict_repr()
            if dict_repr["deleted"]:
                results["data"]["objects"]["deleted"].append(dict_repr)
            else:
                results["data"]["objects"]["placed"].append(dict_repr)

        # add new_placed objects
        for _, pl_obj in self.new_placed_objects.items():
            dict_repr = pl_obj.get_dict_repr()
            if dict_repr["deleted"]:
                results["data"]["objects"]["deleted"].append(dict_repr)
            else:
                results["data"]["objects"]["new_placed"].append(dict_repr)

        # add measurements
        for sensor in self.sensor_list:
            results["data"]["measurements"].append(sensor.get_dict_repr())
        return results



    def fake_everything(self):
        #end=False                                      #to be added later
        #while end==False:
        #    try:
        #        self.mapToSend, Park_area = Seb.get_Park()
        #        area_range = Seb.get_max_square(Park_area)
        #        end=True
        #    except:
        #        pass
        #Places=Seb.get_Messgerät(nr,self.mapToSend, area_range) #returns list of long,lat in the garden

        Park = Polygon([(52.0203613, 8.5270027), (52.0201556, 8.5269901), (52.0198264, 8.5269809), (52.0198275, 8.5268645), (52.0196805, 8.526862), (52.0196753, 8.5270124), (52.019652, 8.5270327), (52.0196275, 8.5270774), (52.0196132, 8.5271464), (52.0196111, 8.527227), (52.0196247, 8.5272853), (52.0196449, 8.5273252), (52.0196714, 8.5273489), (52.0205914, 8.5272813), (52.0206041, 8.5272804), (52.0207697, 8.5273117), (52.0211016, 8.5273649), (52.021134, 8.527373), (52.0211449, 8.5272115), (52.0211369, 8.527186), (52.0207257, 8.5268905), (52.0206219, 8.526816), (52.0203607, 8.5266328), (52.0203613, 8.5270027)])
        Places=[[52.0207102155816, 8.527082210572587],[52.01982376489781,8.527143945722997]]
        print(Park.contains(Point(Places[0][0],Places[0][1])))

        for new_sensor in range(2):
            self.sensor_list.append(Sensor(Places[new_sensor][0],Places[new_sensor][1],[random.random(),(random.random()-0.5)*2+7]))


if __name__ == '__main__':
    Model=Model()

    pass
