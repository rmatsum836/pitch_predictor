import pytest
from automatic_pitch import movement

class TestMovement(object):
    def test_movement(self):
        p_o = [-0.328, 50, 5.978]
        vo = [1.827, -135.5807, -8.338]
        ax = [3.125, 28.682, -12.443]

        movements = movement.calc_movement(p_o, vo, ax)

        p_o = [-0.334, 50, 6.130]
        vo = [2.038, -126.073, -2.344]
        ax = [7.411, 24.514, -32.015]

        movements = movement.calc_movement(p_o, vo, ax)
