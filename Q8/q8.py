import sys
from mathutils import noise

class Q8:
    """Does the math work needed by the quaternion group Q8."""

    def __init__(self, values = None, random = False):
        self.values = values
        self.random = random

        self.q8 = []

        if values:
            if len(values) != 8:
                print("Oops, length of values passed in is wrong. DEATH.")
                sys.exit()
            self.q8 = values

        if random:
            for i in range(0, 8):
                self.q8.append(noise.random())

    def constant_velocity(self, object, q8_delta_position):
        """
        For an object, assigns a delta of position to world position.
        Initially will ignore time
        """
        object.position.x += q8_delta_position[1]
        object.position.y += q8_delta_position[2]
        object.position.z += q8_delta_position[3]
        object.position.x -= q8_delta_position[5]
        object.position.y -= q8_delta_position[6]
        object.position.z -= q8_delta_position[7]
