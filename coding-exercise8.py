
# 1) Function prints 'Hello World!'
def func():
    print("Hello World!")

func()

# 2) Function prints parameter
def func2(name):
    print("Hello my name is {}".format(name))

func2("Google")

# 3) Function takes three arguments x,y,z where z is true it will return x and when z is false it should return y
def func3(x, y, z):
    if z == True:
        return x
    else:
        return y

print(func3("hi", "bye", True))

# 4) Function which returns the product of both the values
def func4(x, y):
    return x*y

print("Product of 2 and 3 is", func4(2, 3))

# 5) Function is_even(), returns boolean
def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False

print("Is the number 2 even?", is_even(2))

# 6) Function that compares if param1 is greater than param2, returns boolean
def func6(x, y):
    if x > y:
        return True
    else:
        return False 

print("Is 2 greater than 3?", func6(2, 3))

# 7) Function which takes arbitrary number of arguments and returns the sum of the arguments
def addNumbers(*nums):
    return sum(nums)

print("addNumbers(1,2,3) =", addNumbers(1,2,3))

# 8) Function which takes arbitrary number of arguments and returns a list containing only the arguments that are even
def evenNumbers(*nums):
    # return [x for x in nums if x % 2 == 0]
    return list(filter((lambda x: x % 2 == 0), nums))

print("Filter [1,2,3,4,5,6] for even numbers:", evenNumbers(1,2,3,4,5,6))

# 9) Function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase
def func9(stringIn):
    result = []
    for x in range(1, len(stringIn)+1):
        if x % 2 == 0:
            result.append(stringIn[x-1].upper())
        else:
            result.append(stringIn[x-1].lower())
    return "".join(result)

print(func9('abcdefghijk'))

# 10) Function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd??

# 11) Function which takes two-strings and returns true if both the strings start with the same letter.
def func11(str1, str2):
    if str1[0] == str2[0]:
        return True
    return False

print(func11("str1", "str2"))

# 12) Given a value,return a value which is twice as far as other side of 7??

# 13) Function that capitalizes first and fourth character of a word in a string.
def func13(stringIn):
    result = []
    for x in range(1, len(stringIn)+1):
        if x == 1 or x == 4:
            result.append(stringIn[x-1].upper())
        else:
            result.append(stringIn[x-1])
    return "".join(result)

print(func13('hello world'))