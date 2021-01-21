import pytest
from automatic_pitch import movement

class TestMovement(object):
    def test_movement(self):
        p_o = [-0.328, 50, 5.978]
        vo = [1.827, -135.5807, -8.338]
        ax = [3.125, 28.682, -12.443]

        movement.calc_movement(p_o, vo, ax)
