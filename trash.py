from probability_calculator import prob_calculator
from probability_calculator.prob_calculator import Hat

hat = prob_calculator.Hat(blue=3, red=2, green=6)
probability = prob_calculator.experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)


