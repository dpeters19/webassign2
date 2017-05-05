import science_utils
import prompter

correct_answer = 100    # TODO change this
correct = False
number_of_submissions = 0
MAX_SUBMISSIONS = 3


while not correct:
    response = prompter.prompt_for_answer("Your answer is: ")
    number_of_submissions += 1
    if science_utils.is_hyper_scientific(response) and science_utils.is_acceptable_answer(correct_answer, response):
        # If response is close enough but not perfect
        if response != science_utils.convert_to_scientific_notation(correct_answer):
            print("You were close enough.")
            print("The correct answer was", science_utils.convert_to_scientific_notation(correct_answer), end=".")

        else:
            print("Your answer was correct!")

        correct = True

    else:
        print("Hmm. Try again. It might just be a matter of your notation.\n")
