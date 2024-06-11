"""
Functions used by the math education game app.
These functions must be called from the main.py file, as appropriate.
"""

import random


def roll_die(low = 1, high = 6):
    ## Making parameters since question didn't say I can't. (For functionality)
    """
    Generates a pseudo-random integer between the 1 and 6, inclusive.
    Use the function random.randint() to generate the pseudo-random number.

    :returns: the pseudo-random integer.
    """
    # complete this function below here
    rand_numb = random.randint(low, high)
    return rand_numb

def get_question_type(breaker = 3):
    ## Didn't specify possibility of the questions, so I'll do a half-split. 
    ## I'll also make a parameter if I ever want to change it, since the question didn't say I can't. A higher number means more chance for addition, vice versa.
    """
    Pseudo-randomly decides whether to give an addition question or a subtraction question.
    Use the function random.randint() to generate a pseudo-random number between 1 and 6, inclusive, that is used to determine the question type.

    :returns: "sum" for an addition question, "difference" for a subtraction question.
    """
    # complete this function below here
    rand_numb = roll_die()
    if rand_numb <= breaker:
        return "sum"
    elif rand_numb > breaker:
        return "difference"

def print_question(die_1_value, die_2_value, question_type):
    """
    Prints out a math question that asks the user to calculate either the sum or difference of the two numbers rolled on virtual dice.

    Follow the given format for each type of question:
    - "You rolled a 3 and a 5... What is the sum of 3 and 5?"
    - "You rolled a 3 and a 5... What is the difference between 3 and 5?"

    A few notes:
    - You must use the format function to plug in the numbers into the printed text template.

    :param die_1_value: The first integer.
    :param die_2_value: The second integer.
    :param question_type: A string - either "sum" or "difference" - indicating whether the user should calculate the sum or difference of the two integers.
    :returns: None
    """
    # complete this function below here
    question_message_sum = "You rolled a {numb_1} and a {numb_2}... What is the sum of {numb_1} and {numb_2}?"
    question_message_dif = "You rolled a {numb_1} and a {numb_2}... What is the difference between {numb_1} and {numb_2}?"
    if question_type == "sum":
        question_message = question_message_sum.format(numb_1 = die_1_value, numb_2 = die_2_value)
    elif question_type == "difference":
        question_message = question_message_dif.format(numb_1 = die_1_value, numb_2 = die_2_value)
    print(question_message)

def input_answer():
    """
    Asks the user to enter their answer to the most recent question.

    A few notes:
    - Remove any leading and trailing whitespace from the user's response.
    - If the user enters a response that is not valid, including empty responses or responses including non-integer characters, return -1.

    :returns: The user's answer, as an int, if valid; or -1 if the user's response was not valid.
    """
    # complete this function below here
    user_answer = input("What's your answer!? ").strip()
    if not user_answer.isdigit():
        return -1
    else:
        return int(user_answer)

def is_correct_answer(die_1_value, die_2_value, question_type, given_answer):
    """
    Determines whether the user's given answer to a question is correct.
    - For difference questions, users are expected to calculate the absolute value of the difference.

    :param die_1_value: The first integer.
    :param die_2_value: The second integer.
    :param question_type: A string - either "sum" or "difference" - indicating whether the user was asked to add or subtract the two integers.
    :returns: True if the user's given answer is correct, False otherwise.
    """
    # complete this function below here
    answer_sum = die_1_value + die_2_value
    answer_dif = abs(die_1_value - die_2_value)
    if question_type == "sum":
    ## I'm under the assumption that die_1_value and die_2_value are already integers
    ###    answer = die_1_value + die_2_value 
    ## UPDATE: I think putting the math operations at the start of the function might actually increase readibility. 
    ## But logically speaking it might increase loading time or something? I dunno
        answer = answer_sum
    elif question_type == "difference":
    ###    answer = abs(die_1_value - die_2_value)
    ## Ditto for given_answer
        answer = answer_dif
    if given_answer == answer:
        return True
    if given_answer != answer:
        return False

def print_congratulations(question_type):
    """
    Congratules the user for answering a question correctly.

    Follow the given format for each type of question:
    - "Yes! Congratulations on the successful addition!"
    - "Yes! Congratulations on the successful subtraction!"

    :param question_type: A string - either "sum" or "difference" - indicating whether the user was asked to add or subtract the two integers.
    """
    # complete this function below here
    ## Could just copy and paste the strings, but I want some fun...
    ## Initially filled the curly braces with operation, but it gave me errors since I was trying to fill it with a variable also named operation?? I assume
    congrats_message = "Yes! Congratulations on the successful {}!"
    if question_type == "sum":
        operation = "addition"
        congrats_message = congrats_message.format(operation)
    elif question_type == "difference":
        operation = "subtraction"
        congrats_message = congrats_message.format(operation)
    print(congrats_message)

def print_correct_answer(die_1_value, die_2_value, question_type):
    """
    Prints the correct answer to the question.

    Follow the given format for each type of question:
    - "No! The sum of 3 and 5 is 8!"
    - "No! The difference between 3 and 5 is 2!"

    :param die_1_value: The first integer.
    :param die_2_value: The second integer.
    :param question_type: A string - either "sum" or "difference" - indicating whether the user was asked to add or subtract the two integers.
    """
    # complete this function below here
    answer_sum = die_1_value + die_2_value
    answer_dif = abs(die_1_value - die_2_value)
    if question_type == "sum":
    ## I'll do this one with f-strings in case I get points taken for formatting in the last instance :<
        print(f"No! The sum of {die_1_value} and {die_2_value} is {answer_sum}!")
    elif question_type == "difference":
        print(f"No! The difference between {die_1_value} and {die_2_value} is {answer_dif}!")

def print_error_message():
    """
    Prints an error message indicating that the user has given an invalid response.

    Follow the given format:
    - "Sorry - that is an invalid answer.  Bye Bye!"
    """
    # complete this function below here
    print("Sorry - that is an invalid answer.  Bye Bye!")
