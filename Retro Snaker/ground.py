# coding:utf-8


class ground(object):
    def __init__(self, size):
        self.size = size
        self.points = list(([None]*size) for i in range(size))

    def add_egg(self, egg):
        self.egg = egg

    def add_snake(self, snake):
        self.snake = snake

    def point_on_snake(self, x, y):
        if x == self.snake.head[0] and y == self.snake.head[1]:
            return True
        else:
            for each_body in self.snake.body:
                if x == each_body[0] and y == each_body[1]:
                    return True
        return False

    def get_empty_points(self):
        return [(x, y) for x in range(self.size) for y in range(self.size) if not self.point_on_snake(x, y)]
