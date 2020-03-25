xnumberone = 0
while xnumberone <= 5:
    print(f"the current value of x is {xnumberone}")
    xnumberone += 1
else:
    print("X is greater than 5.")
honey_Badger = "Honey Badger"
for letter in honey_Badger:
    if letter == " ":
        break
    print(letter)


# def sum_notation(i=0, end=1, f=lambda x: x):
#     return f(i) + sum_notation(i + 1, end, f) if (i <= end) else 0
#
#
# y = lambda x: 1 / (2 ** x)
# print(sum_notation(1, 3))


# def primefactorization1234(num):
#     if int(num) > 1:
#         # check for factors
#         for i in range(2, int(num)):
#             if (num % i) == 0:
#                 print(int(num), "is not a prime number")
#                 print(i, "times", int(num) // i, "is", int(num))
#                 break
#         else:
#             print(int(num), "is a prime number")
#
#
# print(primefactorization1234(int(input("Enter an integer: "))))


def age_function(num1, num2):
    if num1 < 100 and num2 < 100:
        print(str((max(num1, num2))) + " is older.")
    elif num1 >= 100 and not num2 >= 100:
        print("The first person is a centenarian or supercentenarian.")
    elif num2 >= 100 and not num2 >= 100:
        print("The second person is a centenarian or supercentenarian.")
    elif num1 >= 100 and num2 >= 100:
        print("Both people are 100 years or older.")


# print(age_function(float(input("Enter first person's age: ")), float(input("Enter second person's age: "))))


def palindrome_checker(string):
    if list(reversed(string)) == list(string):
        print("Palindrome.")
    else:
        print("Not a Palindrome")


palindrome_checker("racecar")
palindrome_checker("jetbrains")
racecar = "Racecar"


# def sigma(func, start):
#     def function(x):
#         func
#
#     start = x
#     return function(x)
#

# print(sigma(2j+5,1,5))
# sum(5q+2,2,5)
def eliminate_anything_other_than_numbers_and_question_marks(string):
    list_string = [x for x in string]
    liststringnew = []
    for letter in list_string:
        if letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9" or letter == "0" or letter == "?":
            liststringnew.append(letter)
    return liststringnew


def questionmarkssecondtry(string):
    global condition
    liststring = eliminate_anything_other_than_numbers_and_question_marks(string)
    if len(liststring) >= 5:
        for x in range(0, len(liststring) - 4):
            first_position = liststring[x]
            fifth_position = liststring[x + 4]
            if first_position.isdigit() == True and liststring[x + 1] == "?" and liststring[x + 2] == "?" and \
                    liststring[x + 3] == "?" and fifth_position.isdigit() == True:
                if int(first_position) + int(fifth_position) == 10:
                    condition = True
                else:
                    return False
            else:
                condition = False
        if condition:
            return True
        elif condition == False:
            return False
    else:
        return "String does not contain enough numbers and letters"


print(questionmarkssecondtry(input("Enter question marks: ")))
print(112 - 84)


def oldmacdonald(name):
    first_letter_change = name.replace(name[0], name[0].upper())
    fourth_letter_change = first_letter_change.replace(first_letter_change[3], first_letter_change[3].upper(), 1)
    return fourth_letter_change


print(oldmacdonald("macdonald"))
print(2 ** 38)


def calculator(string):
    himyvar = string.replace("*", "")
    return himyvar


print(calculator("5*x"))


def less_than_ten(list1234):
    for x in list1234:
        if x < 5:
            print(x)
        else:
            pass


print(less_than_ten([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))


def divisors(num):
    divisors = []
    for x in range(1, num + 1):
        if num % x == 0:
            divisors.append(x)
    return divisors


print(divisors(56))


def is_prime_number1(num):
    if divisors(num) == [1, num]:
        return f"{num} is prime."
    else:
        return f"{num} is composite."


def is_prime_number2(num):
    if divisors(num) == [1, num]:
        return True
    else:
        return False


print(is_prime_number1(71))
print("is prime number")


def all_prime_numbers_up_to_a_number(num):
    list_of_prime_numbers_up_to_number = []
    for x in range(2, num + 1):
        if is_prime_number2(x) == True:
            list_of_prime_numbers_up_to_number.append(x)
    return list_of_prime_numbers_up_to_number


print(all_prime_numbers_up_to_a_number(72))
print("all prime number")


def prime_factorization(num):
    list_prime_numbers = all_prime_numbers_up_to_a_number(num)
    factors_of_number = []
    for number in list_prime_numbers:
        if num % number == 0:
            factors_of_number.append(number)
    return factors_of_number


print(prime_factorization(144))
# print(prime_factorization(int(input("Enter a number to see its distinct prime factors"))))


import math


def simplification(num):
    prime_factors = prime_factorization(num)
    prime_factors_simplified = []
    for x in prime_factors:
        if x > num / 2:
            pass
        else:
            prime_factors_simplified.append(x)
    return prime_factors_simplified


def mapping(keys, values):
    dictionary = dict(zip(keys, values))
    return dictionary


def hopefully_this_works(num):
    powers = []
    final_powers = []
    prime_factors = simplification(num)
    for p in prime_factors:
        for x in range(1, int(math.log2(num))):
            if num % (p ** x) == 0:
                powers.append(x)
        final_powers.append(max(powers))
        powers.clear()
    return final_powers


def final_factorization(num):
    factors = prime_factorization(num)
    powers = hopefully_this_works(num)
    final_result = mapping(factors, powers)
    return final_result


print(
    "The result will come out like this: {factor:power, factor:power}. For example, twelve (2^2*3) will come out as {2:2,3:1}.")
print(final_factorization(int(input(
    "Enter the number you want to be factored. "))))
print(simplification(18932))
