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
        # self.contents.extend(took)
        return took

    def __str__(self):
        s = ""
        for e in self.contents:
            s += e + " "
        return s


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    true_if_here = []
    for exp in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        for k in expected_balls:
            if drawn.count(k) >= expected_balls[k]:
                true_if_here.append(1)
            else:
                break
    if len(true_if_here) >= len(expected_balls):
        return len(true_if_here) / num_experiments
    else:
        return "ou"

