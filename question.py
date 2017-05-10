import random


def multiple_replace(text, variable_dict):
    for key in variable_dict:
        text = text.replace(key, variable_dict[key])
    return text


last_line = '\n'
question = ""

print("Type in your question here:")
while last_line != "":
    current_line = input()
    if current_line == "":
        break
    question += current_line + "\n"

variables = {}

rand = random.randint

functions = {"rand": rand}

array_of_lines = question.split("\n")

QUESTION_IS_PRESENT = False

for line in array_of_lines:
    if "QUESTION" in line:
        QUESTION_IS_PRESENT = True
        break

if QUESTION_IS_PRESENT:
    variable_lines = []
    question_lines = []

    for index in range(len(array_of_lines)):
        if array_of_lines[index] == "QUESTION":
            QUESTION_INDEX = index
            break

    for index in range(QUESTION_INDEX):
        variable_lines.append(array_of_lines[index])

    for index in range(QUESTION_INDEX + 1, len(array_of_lines)):
        question_lines.append(array_of_lines[index])

    for line in variable_lines:
        variable, value = line.split("=")
        variables["$" + variable] = str(eval(value)).replace("_", " ")

    for line in question_lines:
        question_lines[question_lines.index(line)] = multiple_replace(line, variables)

    for line in question_lines:
        print(line)

# This is the backup method, for when there is no QUESTION line found
else:
    # Calculate values
    for word in array_of_lines:
        if "=" in word:
            variable, value = word.split("=")
            variables["$" + variable] = str(eval(value)).replace("_", " ")

    for words in array_of_lines:
        array_of_lines[array_of_lines.index(words)] = multiple_replace(words, variables)

    for line in array_of_lines:
        if "=" not in line:
            print(line)
