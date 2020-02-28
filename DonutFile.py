from KrispyKreme import Phone

def cube_function(num):
    return float(num) ** 3


print(cube_function(3))
quad=4
def quadfunction(num):
    return float(num)**quad
print(quadfunction(2))
def basketball_score(twopointers,foulshots,threepointers):
    return int(twopointers)*2+int(foulshots)+int(threepointers)
print(basketball_score(1,2,3))
def golf_score(par, number_of_shots):
    if int(number_of_shots) == 1:
        print("Hole in one")
    elif int(par) - int(number_of_shots) == 2:
        print("Eagle")
    elif int(par) - int(number_of_shots) == 1:
        print("Birdie")
    elif int(par) - int(number_of_shots) == 0:
        print("Par")
    elif int(par) - int(number_of_shots) == -1:
        print("Bogey")
    elif int(par) - int(number_of_shots) == -2:
        print("Double Bogey")
    elif int(par) - int(number_of_shots) <= -3:
        print("Go Home!")
    else:
        print("Invalid input. Please enter two integers.")


print(golf_score(5, 9))
secret_word = "Infinity"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
"""
while guess != secret_word and not(out_of_guesses):
   if guess_count < guess_limit:
       guess = input("Enter guess: ")
       guess_count += 1
   else:
       out_of_guesses=True
if out_of_guesses:
    print("Out of guesses. YOU LOSE!")
else:
    print("You win!")
"""


def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(raise_to_power(2, 3))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation = translation + "g"
        elif letter in "AEIOU":
            translation = translation + "G"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
List_of_fruits_file = open("C:\\Users\\peter\\OneDrive\\Documents\\List of Fruits.txt", "w")
List_of_fruits_file.write("\nThis is Python editing this file")
List_of_fruits_file.close()
import aifc

Story_audio = aifc.open("C:\\Users\\peter\\Downloads\\On the Edge of the Dark Sea of Darkness Chapter 6 Part 2.aiff")
print(Story_audio.getnchannels())
Story_audio.close()


class Student:
    def __init__(self, name, major, GPA, is_on_probation, ):
        self.name = name
        self.major = major
        self.GPA = GPA
        self.is_on_probation = is_on_probation


Bob = Student("Bob", "astrophysics", 4.0, False)
print(Bob.name)
Fred = Student("Fred", "Business", 3.5, False)
print(Bob.major)

MyPhone = Phone("Apple", 10, "red", "Castify")
print(MyPhone.colorofphone)


class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year


MyCar = Car("Ford", "Fiesta", "Red", 2020)
print(MyCar.model)
print(MyCar.year)
print(MyCar.color)
things_I_want_for_my_birthday = ["Hiarcs", "Fat Fritz 17 from Chessbase", "a course from Chessbase", "A new mouse",
                                 "a big hard drive", "Brilliant subscription", "Donate $5 to Freecodecamp.org",
                                 "A book by Everyman Chess", "Game Design Software"]
print(things_I_want_for_my_birthday)


import sys

from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
def area_of_a_triangle(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-b))**0.5
    return area
print(area_of_a_triangle(1,2,4))
import cmath
def quadratic_formula_solver(a,b,c):
    x1 = (-b+cmath.sqrt(b**2-4*a*c))/2*a
    x2= (-b-cmath.sqrt(b**2-4*a*c))/2*a
    print("The solutions are " + str(x1)+" and"+str(x2))
print(quadratic_formula_solver(1,2,3))