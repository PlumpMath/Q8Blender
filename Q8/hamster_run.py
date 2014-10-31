import bge
from bge import logic

import csv

def run(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    objects = scene.objects

    if "ran_once" not in own:
        start_position(objects)
        own["ran_once"] = True

def start_position(objects):
    """Sets start positions based on an external csv file."""

    with open("hamster.csv", "r") as h_csv:
        h_csv_reader = csv.reader(h_csv)

        for row in h_csv_reader:
            object_id = row[0]
            x, y, z = row[1], row[2], row[3]
            text_id, text_name = row[4], row[5]

            print("{0} {1} {2} {3} {4} {5}".format(
                object_id, x, y, z, text_id, text_name))

            if object_id in objects:
                objects[object_id].position = \
                        [float(x), float(y), float(z)]

            if text_id in objects:
                objects[text_id].text = text_name
