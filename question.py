import random

import science_utils


def get_question():
    """ Prompts the user to create a question
    Args:
        No parameters
    Returns:
        list: The list of lines to print
        """
    last_line = '\n'
    question = ""

    print("Type in your question here:")
    while last_line != "":
        current_line = input()
        if current_line == "":
            break
        question += current_line + "\n"

    variables = {}

    # Special syntax variables
    rand = random.randint

    array_of_lines = question.split("\n")

    question_is_present = False

    for line in array_of_lines:
        if "QUESTION" in line:
            question_is_present = True
            break

    if question_is_present:
        variable_lines = []
        question_lines = []

        for index in range(len(array_of_lines)):
            if array_of_lines[index] == "QUESTION":
                question_index = index
                break

        for index in range(question_index):
            variable_lines.append(array_of_lines[index])

        for index in range(question_index + 1, len(array_of_lines)):
            question_lines.append(array_of_lines[index])

        for line in variable_lines:
            variable, value = line.split("=")
            variables["$" + variable] = str(eval(value)).replace("_", " ")

        for line in question_lines:
            question_lines[question_lines.index(line)] = science_utils.multiple_replace(line, variables)

        return question_lines

    # This is the backup method, for when there is no QUESTION line found
    else:
        # Calculate values
        for word in array_of_lines:
            if "=" in word:
                variable, value = word.split("=")
                variables["$" + variable] = str(eval(value)).replace("_", " ")

        for words in array_of_lines:
            array_of_lines[array_of_lines.index(words)] = science_utils.multiple_replace(words, variables)

        to_return = []
        for line in array_of_lines:
            if "=" not in line:
                to_return.append(line)
