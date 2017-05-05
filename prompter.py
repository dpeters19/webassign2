import science_utils


def prompt_for_answer(question=""):
    """ Prompts the user for an answer and verifies it
    Args:
        question (String): The question to be displayed to the user
        
    Returns:
        String: The user's answer
    """

    is_acceptable = False
    while not is_acceptable:
        response = input(question)
        try:
            science_utils.convert_to_scientific_notation(response)
            is_acceptable = True
        except ValueError as ve:
            print("{}. Please try again. \n".format(ve.args[0]))

    return response
