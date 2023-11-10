import random


def random_int(min, max):
    """
    Random integer within the specified range.
    """
    return random.randint(min, max)


def random_oprator():
    """
    Random arithmetic operator: '+', '-', '*'
    """
    return random.choice(['+', '-', '*'])


def operation_result(num1, num2, operator):
    """
    Calculate arithmetic problem
    """

    problem = f"{num1} {operator} {num2}"

    if operator == '+': 
        result = num1 + num2
    elif operator == '-': 
        result = num1 - num2
    else: 
        result = num1 * num2
        
    return problem, result

def math_quiz():
    """
    Povide questions and evaluate the answers.
    """

    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = random_int(1, 10)
        num2 = random_int(1, 5)
        operator = random_oprator()

        PROBLEM, CORRECT_ANSWER = operation_result(num1, num2, operator)
        
        print(f"\nQuestion: {PROBLEM}")

        # while loop in order to ensure the introduced number is an integer
        while True:
            try:
                useranswer = int(input("Your answer: "))
                break  # Exit the loop when is successful
            except ValueError:
                print('Please introduce an integer')

        if useranswer == CORRECT_ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)

        else:
            print(f"Wrong answer. The correct answer is {CORRECT_ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
