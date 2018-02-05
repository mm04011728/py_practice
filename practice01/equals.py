class person(object):
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.name == other.name

zhang3 = person("zhang3")
li4 = person("zhang3")

print(zhang3 == li4)