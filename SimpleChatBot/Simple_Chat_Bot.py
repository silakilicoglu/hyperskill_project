# Simple Chat Bot

# function for introducing itself in the consol
def greet(bot_name, birth_year):
    """
    Introducing itself in the consol.

    Parameters:
        bot_name(str): your bot's name
        birht_year(int): your bot's birth year

    """
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + str(birth_year) + '.')

# function for introducing yourself to the bot.
def remind_name():
    """Introducing yourself to the bot."""
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

# function for making the assistant guess your age.
def guess_age():
    """Making the assistant guess your age."""
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

# function for counting
def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

# the assistant will be able to check your knowledge and ask multiple-choice questions
def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To determine the execution time of a program.\n4. To interrupt the execution of a program.\n")
    answer = 2
    user_answer = int(input())
    while user_answer != answer:
        print("Please, try again")
        user_answer = int(input()) 
    print('Completed, have a nice day!')

def end():
    """Show an ending message."""
    print("Congratulations, have a nice day!") 

greet('Aid', 2020)  # change it as you need
remind_name()
guess_age()
count()
test()
end()
