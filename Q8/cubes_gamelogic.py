import bge
from bge import logic

def main(cont):
    own = cont.owner

    scene = logic.getCurrentScene()
    objects = scene.objects
    objects["cube_100"].visible = False
    objects["cube_101"].visible = True
    objects["cube_102"].visible = False

    objects["cube_101"].position.x += 0.1
    objects["cube_101"].position.x -= 0.2