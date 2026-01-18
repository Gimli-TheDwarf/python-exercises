import sys
import random
from collections import defaultdict

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# ratatata = 51111

# def my_function(a , b):
#     global ratatata 
#     ratatata = "idk"
#     result = a + " " +b
#     return result

# garbage = my_function(x, y)
# print(garbage)

# import random

# print(random.randrange(1, 10))

# aaaaaa = str("ilike apples")
# print(aaaaaa[1])

# for x in aaaaaa:
#     print(x, end=" SKADOOSH")

# txt = "here is a text bloack hahah"

# if "block" in txt:
#     print("yes, block word exists")
# else:
#     print("NUH UH")

# slicething = str("HOORAH")
# print(slicething[1:2])
# print(slicething[2:])
# print(slicething[-3: -1])

# print(slicething.lower())

# slicething = str("          RATA OOGH ")
# print(slicething.strip())

# test2 = str("idk even know anymore bro")
# print(test2.split(' '))

# skabam = str("hello my friend")
# print(skabam.replace("h", "######"))

# price = int(12312312312)
# textNew = f"KILL ME {price}"
# print(textNew)
# textNew2 = f"kill me (again) {price:.2f}"
# print(textNew2)
# text3 = "we are the guys who the common folk refer to as  \"pirates\", cool aint it?"
# print(text3.strip())


# print("Enter your name, loser: ")
# x1 = str(input())
# print("Enter your age, stinky: ")
# y1 = int(input())

# def print_greeting(name, age):
#     returnValue = f"Hello, {name}! You are {age} years old (ver old)." 
#     returnValue2 = f"Next, your age will be {age + 1} (even older, wow)"
#     return returnValue, returnValue2

# line1, line2 = print_greeting(x1, y1)
# print(line1)
# print(line2)


# class HumanBeing:
#     def __init__(self, height, weight, sex):
#         self.height = height
#         self.weight = weight
#         self.sex = sex
#     def printSex(self):
#         returnVal = f"Person's biological sex is: {self.sex}"
#         return returnVal
#     def printParams(self):
#         returnVal = f"Person's info \n Height: {self.height} \n Weight: {self.weight}"
#         return returnVal

# humanPerson = HumanBeing(155, 15, "Male")
# line1 = humanPerson.printSex()
# print(line1.strip())

# line2 = humanPerson.printParams()
# print(line2.strip())

# def task1():
#     name = input()
#     last_name = input()
#     age = int(input())
#     return name, last_name, age


# def task1_1(name, last_name, age):
#     name_upper = name.upper()
#     last_name_upper = last_name.upper()
#     line1 = f"Hello, {name_upper} {last_name_upper}!"
#     line2 = f"Next year you will be {age + 1} years old."
#     return line1, line2


# name, last_name, age = task1()
# line1, line2 = task1_1(name, last_name, age)
# print(line1)
# print(line2)

# def task1_2(numb):
#     try:
#         int_number = int(numb)
#     except ValueError:
#         print("Conversion failed")
#         return None
#     else:
#         txt = f"Conversion successful: {int_number}"
#         print(txt)
#         return int_number


# print("Enter a number:")    
# user_number = input()
# result = task1_2(user_number)

# def task2(num):
#     if num >= 90:
#         print("Excellent")
#     elif num >= 75:
#         print("Good")
#     elif num >= 50:
#         print("Satisfactory")
#     else: 
#         print("Fail")
#     return None

# print("Eneter a percentage: ")
# num = int(input())
# task2(num)


# def task2_2(text):
#     if "banana" in text and "apple" in text:
#         returnVal = "two fruits found, pretty cool"
#     elif "apple" in text:
#         returnVal = "Fruit found."
#     elif "banana" in text:
#         returnVal = "Another fruit."
#     else:
#         returnVal = "NO FRUITS."
#     return returnVal

# print("enter text")
# txt = input()
# val = task2_2(txt)
# print(val)


# def task1_2_upgraded(numb):
#     try:
#         int_number = int(numb)

#     except ValueError:
#         print("Conversion failed")
#         return False, None
    
#     else:
#         print(f"Conversion successful: {int_number}")
#         return True, int_number
    

# while True:
#     user_number = input("Enter a number: ")

#     ok, numb = task1_2_upgraded(user_number)

#     if not ok:
#         continue
#     break

# print("You entered a valid int value: ", numb)

#-------------TASK 1-------------
def olympiad_task_1_number_assignment():
    numbs = sys.stdin.read().strip().split()
    numberOfValues = int(numbs[0])
    numbArray = numbs[1:1+numberOfValues]
    return numbArray

def olympiad_task_1_number_sorting(array):
    return sorted(array ,key=lambda element: (element[::-1], len(element))) #first compare reverse numbers, if those are equal compare length 

numbersArray = olympiad_task_1_number_assignment()
sortedArray = olympiad_task_1_number_sorting(numbersArray)

sys.stdout.write("\n".join(sortedArray))
#--------------------------------

#-------------TASK 2-------------
def distinct_count(number: str) -> int:
    num = len(set(number))
    return num

def olympiad_task_2():
    numbs = sys.stdin.read().strip().split()
    numberOfValues = int(numbs[0])
    numbsArray = numbs[1:1+numberOfValues]
    return numbsArray

def olympiad_task_2_part_2(array):
    array.sort(key=lambda element: (element[-1], distinct_count(element), len(element), element), reverse=False)
    return array

thing = olympiad_task_2()
sortedArrayed2 = olympiad_task_2_part_2(thing)

sys.stdout.write("\n".join(sortedArrayed2))
#--------------------------------

#-------------TASK 3 UNSOLVED-------------
def olympiad_task_3():
    nums = sys.stdin.read().strip().split()
    first = int(nums[0])
    second = int(nums[1])
    numsArray = list(map(int, nums[2:2+first]))
    lenArr = int(len(numsArray))
    ans = int(0)

    for x in range(len(numsArray)):
        arr2 = numsArray[x:lenArr]
        len2 = int(len(arr2))

        for i in range(len(arr2)):
            sum1 = sum(arr2[i:len2]) % second
            if int(sum1) == 0:
                ans +=1

    sys.stdout.write(str(ans))

olympiad_task_3()
# #--------------------------------

#-------------TASK 4-------------
def olympiad_task4(N: int, M: int, K: int) -> None:
    array = list(range(1, N+1))
    index = (M % N)
    #start counting after element

    for i in range(N):
        remove = (index + (K-1)) % len(array)
        x = array.pop(remove)
        print(x, end=" ")
        index = remove % len(array)

arr = sys.stdin.read().strip().split()
N = arr[0]
M = arr[1]
K = arr[2]
olympiad_task4(N,M,K)
#--------------------------------

#-------------TASK 5-------------
def olympiad_task5(cc, c):

    groups = defaultdict(list)
    completeList = {}
    #c = list(dict.fromkeys(c))
    for i, el in enumerate(c[:-1]):
        tempArray = c[i+1:] #solve this later
        for el2 in tempArray:
            val = el + el2
            groups[val].append((el, el2)) 

    for key, value in groups.items():
        # 4: [(2,2),(3,1)]
        flatValue = []
        for a,b in value:
            flatValue.extend([a,b])

        unique = set(flatValue)

        if int(len(unique)) > 2:
            completeList[key].append(unique)

    if int(len(completeList)) > 0:
        sys.stdout.write("1\n", random.choice(completeList))
    else:
        sys.stdout.write("0")

arr = sys.stdin.read().strip().split()
cardCount = int(arr[0])
cards = arr[1:cardCount+1]
olympiad_task5(cardCount, cards)
#--------------------------------