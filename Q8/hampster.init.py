#!/usr/bin/env python
import bge
from bge import logic

import csv

object_names = {}
object_positions = {}

def init(cont)
    own = cont.owner
    scene = logic.getCurrentScene()
    objects = scene.objects

    with open("hampster.csv", "r") as hcsv:
        hcsv_reader = csv.reader(hcsv)

        for row in hcsv_reader:
            object_id = row[0]
            object_name = row[1]        
            x, y z = row[2], row[3], row[4]

            if object_id in objects:
                objects[object_id].position.x = x
                objects[object_id].position.y = y
                objects[object_id].position.x = z

