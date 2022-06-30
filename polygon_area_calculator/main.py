import polygon_area_calculator
from unittest import main


rect = polygon_area_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = polygon_area_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_module', exit=False)


# Run unit tests automatically
main(module='test_module', exit=False)

# rect = polygon_area_calculator.Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())
#
# sq = polygon_area_calculator.Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())
#
# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))

