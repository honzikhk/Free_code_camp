import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.took = []
        for key in kwargs:
            for each in range(kwargs[key]):
                self.contents.append(key)
        self.original_data = self.contents.copy()       # need this to restart_variables

    def restart_variables(self):
        self.contents = self.original_data.copy()
        self.took.clear()

    def draw(self, number_of_balls):
        if number_of_balls >= len(self.contents):
            return self.contents
        for i in range(number_of_balls):
            random_index = random.randint(0, len(self.contents) - 1)
            draw = self.contents.pop(random_index)
            self.took.append(draw)
        return self.took

    def __str__(self):
        s = ""
        for e in self.contents:
            s += e + " "
        return s


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_lst = []
    for key in expected_balls:
        for each in range(expected_balls[key]):
            expected_balls_lst.append(key)
    successful_experiments = 0
    for exp in range(num_experiments):
        hat.restart_variables()
        print(hat.contents)
        drawn = hat.draw(num_balls_drawn)
        cnt = 0
        for e in expected_balls_lst:
            if expected_balls_lst.count(e) <= drawn.count(e):
                cnt += 1
            else:
                break
        if len(expected_balls_lst) == cnt:
            successful_experiments += 1
        else:
            continue
    return successful_experiments / num_experiments
