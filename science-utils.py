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
