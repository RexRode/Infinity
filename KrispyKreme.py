import pandas as pandas


def square_function(number):
    return number * number


print(square_function(7))


class Phone:
    def __init__(self, brand, version, colorofphone, phonecase):
        self.brand = brand
        self.version = version
        self.colorofphone = colorofphone
        self.case = phonecase


class Person:
    def __init__(self, is_hungry, favorite_food, name):
        self.is_hungry = is_hungry
        self.favorite_food = favorite_food
        self.name = name


bob = Person(True, "Pancakes", "Bob")
jim = Person(True, "noodles", "Jim")


def hungry(p):
    # enter something with the class Person
    if type(p) == Person:
        if p.is_hungry:
            return (p.name + " eats " + p.favorite_food + ".")
        else:
            return (p.name + " is not hungry.")


print(hungry(bob))
print(hungry(jim))


def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    elif num1 % 2 != 0 or num2 % 2 != 0:
        return max(num1, num2)


print(lesser_of_two_evens(5, 7))


def animal_crackers(string1, string2):
    if string1[0] == string2[0]:
        return True
    else:
        return False


print(animal_crackers("Crazy", "Cats"))


def OldMacDonald(name):
    firstletter = name[0]
    firstletter.capitalize()
    fourthletter = name[3]
    fourthletter.capitalize()
    for x in name:
        if name.index(x) == 0:
            x = firstletter
        if name.index(x) == 3:
            x = fourthletter
    return name


print(OldMacDonald("macdonald"))


def makes_twenty(integer1, integer2):
    if integer1 == 20 or integer2 == 20:
        return True
    elif integer2 + integer1 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))


def name_and_age(name, age):
    centennial_year = str(2020 - float(age) + 100)
    print(f"{name} will turn 100 in the year {centennial_year}")


'''print((name_and_age(input("Enter your name: "), input("Enter your age: "))))'''

'''def capital_indexes(string1):
    def slicing(string):
        x = 0
        slicing_string = []
        for integer1 in range(x, len(string)):
            slicing_string.append(string[integer1])
            x += 1
        return (slicing_string)

def questionmarks(string1):
    mylist = [x for x in string1]
    questionmarkindex = mylist.index("???")
    number =
    numberindex = mylist.index(f"{number}")'''


def masteryoda(string1):
    splitstring1 = string1.split()[::-1]
    return " ".join(splitstring1)


print(masteryoda("I am home"))


def almost_there(num1):
    if abs(200 - num1) <= 10 or abs(100 - num1) <= 10:
        return True
    else:
        return False


print("almost there")
print(almost_there(90))
print(almost_there(111))
print(almost_there(190))
print(almost_there(220))


def find_33(nums):
    x: int
    for x in range(-len(nums) + 1, 0):
        if nums.pop(x) == nums.pop(x + 1) == 3:
            return True
        else:
            return False
print("eliminate")

def eliminate_anything_other_than_numbers_and_question_marks(string):
    list_string = [x for x in string]
    liststringnew = []
    for l in list_string:
        if l == "1" or l == "2" or l == "3" or l == "4" or l == "5" or l == "6" or l == "7" or l == "8" or l == "9" or l == "0" or l == "?":
            liststringnew.append(l)
        else:
            pass

    return (liststringnew)

def questionmarkssecondtry(string):
    global condition
    liststring = eliminate_anything_other_than_numbers_and_question_marks(string)
    for x in range(0,len(liststring)-5):
        if liststring[x].isdigit()==True and liststring[x+4].isdigit()==True:
            if int(liststring[x])+int(liststring[x+4])==10:
                condition = True
            else:
                return False
    if condition:
        return True
    '''for x in range(0,20):
        if int(liststring[x])+int(liststring[x+4])==10:
            return True
        else:
            return False'''
print("questionmarks")
print(questionmarkssecondtry("arrb6???4xxbl5???eee5wqu7???3"))
print(questionmarkssecondtry("acc?7??sss?3rr1??????5"))
print(eliminate_anything_other_than_numbers_and_question_marks("arrb6???4xxbl5???eee5"))
print(find_33([1, 3, 3]))
print("\u265e")

def indexing(lengthystring):
    print(len(lengthystring))
    for x in range(len(lengthystring)*-1+1,1):
        print(x)
print(indexing("Ilikepieanddonutsandjetbrainsandpycharm"))
# else:
# liststringpop = list_string.pop(liststringpop.index(x))

# if liststring.pop(x)+liststring.pop(0)==10:
# digits = True
"""Steps:
step 0: create a string out of the list
Step 1: Find the index of "???" in the string.
Step 2: subtract 1 from that """