class animal(object):
    def __init__(self, name):
        self.name = name
    def call(self):
        print("call")
class cat(animal):
    def call(self):
        print("miao "*3)

class dog(animal):
    def call(self):
        print("wang "*3)
class toy(object):
    def call(self):
        print("ling "*3)

def call(animal):
    animal.call()


# animal111 = animal("aaa")

# print(animal111.name)
cat1= cat("miao1")
dog1 = dog("wang1")
toy1 = toy()
call(cat1)
call(dog1)
call(toy1)
