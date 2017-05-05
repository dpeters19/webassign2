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
    try:
        float(number)
    except TypeError as te:
        raise TypeError("That was not a number")
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


def generate_acceptable_answers(correct_answer):
    """ Calculates acceptable answers (answers accurate to e+1)
    Args:
         correct_answer (float)

    Returns:
         list of len 3

    Example:
    >>> generate_acceptable_answers(5)
    ['4.99e0', '5.00e0', '5.01e0']
    >>> generate_acceptable_answers(50)
    ['4.99e1', '5.00e1', '5.01e1']
    >>> generate_acceptable_answers(1001)
    ['9.90e2', '1.00e3', '1.01e3']
    >>> generate_acceptable_answers(0.03)
    ['2.99e-2', '3.00e-2', '3.01e-2']
    """
    correct_answer = convert_to_scientific_notation(correct_answer)
    number, exponent = correct_answer.split("e")
    number = float(number)
    max_number = number + .01
    min_number = number - .01
    max_number = str(max_number) + "e" + exponent
    min_number = str(min_number) + "e" + exponent

    min_number = convert_to_scientific_notation(float(min_number))
    correct_answer = convert_to_scientific_notation(float(correct_answer))
    max_number = convert_to_scientific_notation(float(max_number))

    return [min_number, correct_answer, max_number]


def is_acceptable_answer(acceptable_answers, response):
    """ Determines if an answer is within the range of acceptable answers
    Args:
        acceptable_answers (list(String))
        response (String)

    Returns:
        bool: True of the answer is acceptable, false otherwise

    """
    response = float(response)
    min_value = float(acceptable_answers[0])
    max_value = float(acceptable_answers[-1])

    if min_value <= float(response) <= max_value:
        return True

    return False
