# coding:utf-8
from random import *


class egg(object):
    def __init__(self, ground):
        self.ground = ground
        ground.add_egg(self)
        self.position = None

    def refresh(self):
        empty_points = self.ground.get_empty_points()
        lenth = len(empty_points)
        num = randint(0, lenth - 1)
        self.move(empty_points[num])

    def move(self, new_point):
        self.position = new_point
