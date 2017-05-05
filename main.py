import science_utils

correct_answer = 100    # TODO change this
acceptable_answers = science_utils.generate_acceptable_answers(correct_answer)
correct = True
number_of_submissions = 0
MAX_SUBMISSIONS = 3
while not correct and number_of_submissions < MAX_SUBMISSIONS:
    response = input("Your answer is: ")
    number_of_submissions += 1
    if science_utils.is_hyper_scientific(response) and science_utils.is_acceptable_answer(acceptable_answers, response):
        correct = True
        print("Your answer was correct (or close enough)")

    else:
        print("Hmm. Try again. It might just be a matter of your notation.\n")
