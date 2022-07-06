from probability_calculator.prob_calculator import Hat

expected_balls = {"blue": 2, "red": 1}
drawn = ['green', 'green', 'blue', 'red']


haf = Hat(blue=4, red=2, green=6)
print(haf.draw(11))
