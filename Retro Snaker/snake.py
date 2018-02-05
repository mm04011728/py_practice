class snake(object):
    def __init__(self):
        self.head = (2, 0)
        self.body = []
        self.body.append((0, 0))
        self.body.append((1, 0))
        self.angle = 0
        self.is_dead = False

    def move(self):
        pass

    def eat(self, egg):
        pass

    def grown(self):
        pass

    def turn_left(self):
        self.angle -= 90

    def turn_right(self):
        self.angle += 90

    def front_is_egg(self):
        pass

    def front_is_clear(self):
        pass

    def die(self):
        self.is_dead = True
