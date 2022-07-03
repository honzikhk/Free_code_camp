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


def experiment(hatf, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    print(f"hatf.draw: {hatf.draw(num_balls_drawn)}")
    for exp in range(num_experiments):
        for k, v in expected_balls:
            true_if_here = 0
            if expected_balls[k] >= hatf.draw(num_balls_drawn).count(expected_balls[v]):
                true_if_here += 1
        if true_if_here == len()
    return m / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hatf=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)


# hat1 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print(hat1.contents)
# print(hat1.draw(2))
print(f"Probability is: {probability}")
