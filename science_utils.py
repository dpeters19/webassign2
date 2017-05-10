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
    pattern = r"\d\.\d{2}e\d{1,}"
    if re.search(pattern, number) is not None:
        if number[0] != "0":  # First number should never be zero
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

    min_number = int(float(min_number))
    max_number = int(float(max_number))

    if min_number <= int(float(response)) <= max_number:
        return True

    return False


def multiple_replace(text, variable_dict):
    """

    Args:
        text (str): The text to replace keys with values
        variable_dict (dict): The dictionary that holds the keys and values

    Returns:
        str: Text with the keys replaced with values

    Examples:
        >>> multiple_replace("A B C a b c", {"a":10, "A": 10})
        '10 B C 10 b c'
    """
    for key in variable_dict:
        text = text.replace(key, str(variable_dict[key]))
    return text
