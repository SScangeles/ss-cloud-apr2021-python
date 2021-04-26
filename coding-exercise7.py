
# 1) Find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
div7_notMult5 = [num for num in range(
    1500, 2701) if num % 7 == 0 and num % 5 == 0]
print(div7_notMult5)

# 2) Convert celsius to and from fahrenheit
def celToFah(temperature):
    fah = (float(temperature)*9/5) + 32
    print("{}\N{DEGREE SIGN}C is {}\N{DEGREE SIGN}F".format(float(temperature), fah))

def fahToCel(temperature):
    cel = (float(temperature)-32) * 5/9
    print("{}\N{DEGREE SIGN}C is {}\N{DEGREE SIGN}F".format(float(temperature), cel))

print()
celToFah(30)
fahToCel(86)

# 3) Guess that number!
import random
def guessGame():
    while True:
        randnum = random.randrange(1, 10)
        num = input()
        if (int(num) == randnum):
            print('Well guessed!')
            break
        else:
            print('Try again. Random number:', randnum)

# print('\nEnter a number to guess:')
# guessGame()

# 4) Pattern
def mypattern(n):
    for x in range(1, n+1):
        print("* "*x)
    for x in range(n-1, 0, -1):
        print("* "*x)

print()
mypattern(5)

# 5) Reverse input
print("\nEnter string to reverse:")
input5 = input()
print(input5[::-1])

# 6) Count even and odd numbers
numlist = [x for x in range(1, 10)]
even = 0
odd = 0
for x in numlist:
    if (x%2) == 0: even += 1
    else: odd += 1

print("\nList of numbers:", numlist)
print("Even count:", even)
print("Odd count:", odd)

# 7) Print mixed list datatypes
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
print('\nDatalist:', datalist)
for x in datalist:
    if type(x) == tuple:
        print("Tuple: ", x)
    elif type(x) == list:
        print("List: ", x)
    elif type(x) == float:
        print("Float: ", x)
    elif type(x) == complex:
        print("Complex: ", x)
    elif type(x) == str:
        print("String: ", x)
    elif type(x) == dict:
        print("Dictionary: ", x)
    elif type(x) == bool:
        print("Boolean: ", x)
    elif type(x) == int:
        print("Integer: ", x)

# 8) Print 0-6 except 3 and 6
print("\nNumbers 0-6 except 3 and 6:")
for x in range(7):
    if x != 3 and x != 6:
        print(x, end=" ")
print()
