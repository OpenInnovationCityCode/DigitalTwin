# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import overpy
import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
import random


def get_Park():  # returns the real values of the park outside from the Internett
    api = overpy.Overpass()
    # fetch all ways in square (...,...,...,...)

    result = api.query("""way (52.019420, 8.526294, 52.021246, 8.527599);out;""")
    # print(result.get_ways())
    Park = result.get_way(37872243)
    # print(Park)
    #print(type(Park))
    #print(Park)
    #print(" ")
    Park_nodes = (Park.get_nodes(resolve_missing=True))

    area_nodes = np.zeros((2, len(Park.get_nodes()))).T
    area_nodes_list = []

    i = 0
    for node in Park_nodes:
        # id = node.
        # print(node)
        area_nodes[i][0] = node.lat
        area_nodes[i][1] = node.lon
        area_nodes_list.append((area_nodes[i][0], area_nodes[i][1]))

        i += 1

    polygon = Polygon(area_nodes_list)

    return polygon, area_nodes


def get_max_square(Park_area):  # get the maximal and minimal Lat &Long of the Park
    x_range = [min(Park_area[:, 0]), max(Park_area[:, 0])]
    y_range = [min(Park_area[:, 1]), max(Park_area[:, 1])]

    return [x_range, y_range]


def get_Messgerät(nr, Park, area_range):  # returns nr an Punkten im Park
    result = []
    while len(result) < nr:
        x = random.uniform(area_range[0][0], area_range[0][1])
        y = random.uniform(area_range[1][0], area_range[1][1])

        if Park.contains(Point(x, y)):
            result.append([x, y])
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    Park,Park_area=get_Park()
    area_range=get_max_square(Park_area)

    #print(area_range)
    #print(get_Messgerät(5,Park,area_range))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
