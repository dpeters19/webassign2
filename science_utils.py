import re

def is_hyper_scientific(number):
    """ Determines if an answer is hyper-scientific
    Args:
        number (String)
    Returns:
        bool: True if is hyper-scientific, False otherwise
    Example:
    >>> is_hyper_scientific("1.00e2")
    True
    >>> is_hyper_scientific("100")
    False
    >>> is_hyper_scientific("1.234e5")
    False
    """
    if convert_to_scientific_notation(float(number)) == number:
        return True
    return False


def convert_to_scientific_notation(number):
    """ Converts a number to scientific notation
    Args:
         number (float)

    Returns:
         String

    Example:
    >>> convert_to_scientific_notation(5)
    '5.00e0'
    >>> convert_to_scientific_notation(10)
    '1.00e1'
    >>> convert_to_scientific_notation(-100)
    '-1.00e2'
    >>> convert_to_scientific_notation(0.01)
    '1.00e-2'
    """

    pattern = r"\d\.\d{2}e\d"

    if re.search(pattern, number) is None:
        raise ValueError("That was not a number")

    number = "%.2e" % number
    if "+" in number:
        positive = True
        number, exponent = number.split("+")
    else:
        positive = False
        number, exponent = number.split("-")

    exponent = str(int(exponent))  # Removes leading zeros

    if positive:
        return number + exponent
    else:
        return number + "-" + exponent


def is_acceptable_answer(correct_answer, response):
    """ Calculates if an answer is an acceptable distance from the correct answer
    Args:
        correct_answer (float)
        response (String)

    Returns:
        bool: True of the answer is an acceptable answer, false otherwise

    Examples:
    >>> is_acceptable_answer(100, '1.00e2')
    True
    >>> is_acceptable_answer(100, '1.01e2')
    True
    >>> is_acceptable_answer(100, '1.02e2')
    False
    """

    # TODO Handle errors better with loop
    try:
        correct_answer = convert_to_scientific_notation(correct_answer)
    except ValueError as ve:
        print(ve.args)

    number, exponent = correct_answer.split("e")
    number = float(number)
    max_number = number + .01
    min_number = number - .01
    max_number = str(max_number) + "e" + exponent
    min_number = str(min_number) + "e" + exponent

    min_number = float(min_number)
    correct_answer = float(correct_answer)
    max_number = float(max_number)

    if min_number <= float(response) <= max_number:
        return True

    return False
