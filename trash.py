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
            took.append(self.contents.pop(random.randint(0, len(self.contents) - len(took) - 1)))
        self.contents.extend(took)
        return took

    def __str__(self):
        return self.contents


def experiment(hatf, expected_balls, num_balls_drawn, num_experiments):
    #m = 0
    for exp in range(num_experiments):
        drawn = hatf.draw(num_balls_drawn)
        # black = hatf.contents.count("black")
        # red = hatf.contents.count("red")
        # green = hatf.contents.count("green")
        # print(f"{hatf.contents}, black: {black}, red: {red}, green: {green}")
        # print(f"vytazeno z klobouku: {drawn}")
        true_if_here = []
        for k in expected_balls:
            if expected_balls[k] >= drawn.count(k):
                true_if_here.append(1)
            else:
                break
        if len(true_if_here) >= len(expected_balls):
            return len(true_if_here) / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hatf=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

hat2 = Hat(white=10)
probability2 = experiment(hatf=hat2,
                          expected_balls={"white": 1},
                          num_balls_drawn=2,
                          num_experiments=10)



# hat1 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print(hat1.contents)
# print(hat1.draw(2))
print(f"Probability is: {probability}")
print(f"Probability2 is: {probability2}")
