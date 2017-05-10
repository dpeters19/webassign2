import prompter
import question
import science_utils

correct = False
number_of_submissions = 0
MAX_SUBMISSIONS = 3

question, correct_answer = question.get_question()

for line in question:
    print(line)
print(correct_answer)

while not correct and number_of_submissions < MAX_SUBMISSIONS:
    response = prompter.prompt_for_answer("Your answer is: ")
    number_of_submissions += 1

    # Checks if answer is right but notation is wrong
    if not science_utils.is_hyper_scientific(response):

        # Determines if the answer is numerically correct
        try:
            if science_utils.is_acceptable_answer(correct_answer,
                                                  science_utils.convert_to_scientific_notation(float(response))):
                print("Your answer is right, but your notation is wrong. \nPlease try again.")

            continue
        except ValueError as ve:
            print("That was not a number. Please try again")
            continue

    if science_utils.is_acceptable_answer(correct_answer, response):
        # If response is close enough but not perfect
        if response != science_utils.convert_to_scientific_notation(int(correct_answer)):
            print("You were close enough.")
            print("The correct answer was", science_utils.convert_to_scientific_notation(correct_answer), end=".")

        else:
            print("Your answer was correct!")

        correct = True
    else:
        # The answer is not numerically correct
        print("Hmm. Try again.")

if number_of_submissions == MAX_SUBMISSIONS:
    print("Make a note that you need help answering this type of question.")
