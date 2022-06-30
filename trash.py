import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs:
            for each in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, number_of_balls):
        if number_of_balls >= len(self.contents):
            return self.contents
        took = []
        for each in range(number_of_balls):
            took.append(self.contents.pop(random.randint(0, len(self.contents) - len(took))))
        return took

    def __str__(self):
        return self.contents


hat1 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
print(hat1.contents)
print(hat1.draw(2))

