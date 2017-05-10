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


variable_lines = []
question_lines = []

variables = {}

rand = random.randint

functions = {"rand": rand}

# This is the backup method, for when there is no QUESTION line found

array_of_lines = question.split("\n")

# Calculate values
for word in array_of_lines:
    if "=" in word:
        variable, value = word.split("=")
        variables["$" + variable] = str(eval(value)).replace("_", " ")

for words in array_of_lines:
    array_of_lines[array_of_lines.index(words)] = multiple_replace(words, variables)

for words in array_of_lines:
    # TODO find a way to print array_of_lines
    exec("print(" + words + ")")
