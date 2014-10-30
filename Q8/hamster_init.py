import bge
from bge import logic

import csv

def start_position(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    objects = scene.objects

    object_names = {}
    object_positions = {}

    with open("hamster.csv", "r") as hcsv:
        hcsv_reader = csv.reader(hcsv)

        for row in hcsv_reader:
            object_id = row[0]
            object_name = row[1]
            x, y, z = row[2], row[3], row[4]

            print("{0} {1} {2} {3} {4}".format(
                    object_id, object_name, x, y, z))

            if object_id in objects:
                objects[object_id].position = [float(x), float(y), float(z)]

