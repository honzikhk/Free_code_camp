
def arithmetic_arranger(data, answer=False):
    if too_many_problems(data):
        return "Error: Too many problems."
    split = split_data(data)
    if forbidden_operators(split):
        return "Error: Operator must be '+' or '-'."
    if contain_bad_character(split):
        return "Error: Numbers must only contain digits."
    if operand_has_more_then_4_digits(split):
        return "Error: Numbers cannot be more than four digits."
    first_row = format_first_row(split)
    second_row = format_second_row(split)
    third_row = format_third_row(split)
    if answer:
        fourth_row = format_fourth_row(split)
        return f"{first_row}\n{second_row}\n{third_row}\n{fourth_row}"
    return f"{first_row}\n{second_row}\n{third_row}"


def too_many_problems(data):
    if len(data) > 5:
        return True


def forbidden_operators(data):
    for problem in data:
        if problem[1] == "*" or problem[1] == "/":
            return True


def contain_bad_character(data):
    for problem in data:
        for char in problem[0]:
            if char.isdigit():
                continue
            else:
                return True
        for char in problem[2]:
            if char.isdigit():
                continue
            else:
                return True
    return False


def operand_has_more_then_4_digits(data):
    for problem in data:
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return True
    return False


def split_data(data):
    return [problem.split() for problem in data]


def count_length_of_row(data):
    longest_part = len(max(data, key=len))
    length_of_row = longest_part + 2
    return length_of_row


def format_first_row(data):
    row = ""
    for problem in data:
        row += format_elements_in_first_row(problem)
    return row.rstrip()


def format_elements_in_first_row(problem):
    length_of_row = count_length_of_row(problem)
    element = (length_of_row - len(problem[0])) * " " + problem[0] + 4 * " "
    return element


def format_second_row(data):
    row = ""
    for problem in data:
        row += format_elements_in_second_row(problem)
    return row.rstrip()


def format_elements_in_second_row(problem):
    length_of_row = count_length_of_row(problem)
    element = problem[1] + (length_of_row - (len(problem[2]) + 1)) * " " + problem[2] + 4 * " "
    return element


def format_third_row(data):
    row = ""
    for problem in data:
        row += format_elements_in_third_row(problem)
    return row.rstrip()


def format_elements_in_third_row(problem):
    length_of_row = count_length_of_row(problem)
    row = length_of_row * "-" + 4 * " "
    return row


def format_fourth_row(data):
    row = ""
    for problem in data:
        if problem[1] == "+":
            number = str(int(problem[0]) + int(problem[2]))
            row += format_elements_in_fourth_row(problem, number)
        elif problem[1] == "-":
            number = str(int(problem[0]) - int(problem[2]))
            row += format_elements_in_fourth_row(problem, number)
    return row.rstrip()


def format_elements_in_fourth_row(problem, number):
    length_of_row = count_length_of_row(problem)
    element = (length_of_row - len(number)) * " " + number + 4 * " "
    return element


# print(arithmetic_arranger(['3801 - 2', '123 + 49'], True))
