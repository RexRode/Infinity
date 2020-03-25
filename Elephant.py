alphabet = "abcdeghijklmnopqrstuvwxyz"
print(alphabet.find("g"))
print(alphabet.find("i"))


def translate(string):
    newstring = ""
    for element in string:
        if element != " ":
            newstring.append(element)
    for letter in newstring:
        index_of_letter = alphabet.find(letter)
        print(alphabet[index_of_letter + 2])


# print(translate(input("Enter thing to translate: ")))
def sigma(func, start, end):
    value = sum([(print(func)) for x in range(start, end)])
    return value


import math
# print(sigma("5x", 1, 10))
import random
print("Python Challenges")


def list_overlap(l1, l2):
    l3 = []
    for x in l1:
        if x in l1 and x in l2:
            l3.append(x)
    return l3


print(list_overlap([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))


def cows_and_bulls():
    secret_number = random.randint(1000, 9999)
    guess = ""
    cows = 0
    bulls = 0
    number_of_guesses = 0
    print("Guess a number between and including 1000 and 9999. A cow is a correct digit in the correct place. A bull is anything else.")
    while guess != secret_number:
        guess = int(input("Enter guess: "))
        guess_thousands = guess // 1000
        guess_hundreds = (guess % 1000) // 100
        guess_tens = ((guess % 1000) % 100) // 10
        guess_ones = (((guess % 1000) % 100) % 10) // 1
        thousands_digit_secret = secret_number // 1000
        hundreds_secret = (secret_number % 1000) // 100
        secret_tens = ((secret_number % 1000) % 100) // 10
        secret_ones = (((secret_number % 1000) % 100) % 10) // 1
        if thousands_digit_secret == guess_thousands:
            cows += 1
        else:
            bulls += 1
        if hundreds_secret == guess_hundreds:
            cows += 1
        else:
            bulls += 1
        if guess_tens == secret_tens:
            cows += 1
        else:
            bulls += 1
        if guess_ones == secret_ones:
            cows += 1
        else:
            bulls += 1
        number_of_guesses += 1
        result = f"You have {cows} cows and {bulls} bulls. You have guessed {number_of_guesses} times."
        print(result)
        bulls = 0
        cows = 0
    if guess == secret_number:
        print("You guessed the secret number! You win!")


print(cows_and_bulls())
