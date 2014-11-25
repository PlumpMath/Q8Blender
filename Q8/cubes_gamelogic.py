import bge
from bge import logic
import q8
import settings

def main(cont):
    own = cont.owner

    scene = logic.getCurrentScene()
    objects = scene.objects
    objects["cube_100"].visible = True
    objects["cube_101"].visible = True
    objects["cube_102"].visible = True

    d1 = [0.001, 0.0005, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008]
    qd1 = q8.Q8(random = True)
    qd1.constant_velocity(objects["cube_102"], d1)
    qd1.constant_velocity(objects["cube_101"], d1)
    qd1.constant_velocity(objects["cube_100"], d1)

    # A cyclic timer

    if not 'timer' in own:
        own['timer'] = 0

    repeat_after = 600

    if own['timer'] == 0:
        set_initial_position(objects)

    own['timer'] += 1
    own['timer'] %= settings.CYCLE_LENGTH

    print(own['timer'])


def set_initial_position(objects):
    """Use values in settings to set position of objects."""

    object_names = ["cube_100", "cube_101", "cube_102"]

    for object_name in object_names:
        objects[object_name].position.x = settings.INITIAL_POSITION[object_name][1]
        objects[object_name].position.y = settings.INITIAL_POSITION[object_name][2]
        objects[object_name].position.z = settings.INITIAL_POSITION[object_name][3]
        objects[object_name].position.x -= settings.INITIAL_POSITION[object_name][5]
        objects[object_name].position.y -= settings.INITIAL_POSITION[object_name][6]
        objects[object_name].position.z -= settings.INITIAL_POSITION[object_name][7]
