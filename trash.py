from probability_calculator import prob_calculator
from probability_calculator.prob_calculator import Hat

hat = prob_calculator.Hat(red=5, blue=2)
actual = hat.draw(2)


print(len(hat.contents))




