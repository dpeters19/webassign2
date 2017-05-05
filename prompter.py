def prompt_for_answer(question=""):
    """ Prompts the user for an answer
    Args:
        question (String): The question to be displayed to the user
        
    Returns:
        String: The user's answer
    """

    # TODO Change to verify answer here
    response = ""
    while response == "":
        response = input(question)
    return response
