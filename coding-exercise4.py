
# Coding exercises:
# 1) List of ...
list1 = [1, "hello world", 3.14]
print(list1)

# 2) List of [1,1[1,2]], grab 2
list2 = [1, 1, [1, 2]]
print(list2[2][1])

# 3) print list[1:]
list3 = ["a", "b", "c"]
print(list3[1:])

# 4) create dictionary and assign to var
week = {
    "sunday": 1,
    "monday": 2,
    "tuesday": 3,
    "wednesday": 4,
    "thursday": 5,
    "friday": 6,
    "saturday": 7
}

day = week["sunday"]
print("Sunday is day:", day)

# 5) Dictionary output
dictionaryList = {"k1": [1, 2, 3]}
print(dictionaryList["k1"][1])

# 6) list to tuple
list5 = [1, [1, 2]]
tuple5 = (list5[0], list5[1])
print(tuple5)

# 7) Mississippi to distinct character word
set7 = set("Mississippi")
print("".join(set7))

# 8) Add "X" to set above?
set7.add("X")
print(set7)

# 9) Output set
set9 = set([1, 2, 3, 4])
set9.add(1)
print(set9)

# Question: 1) Find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
div7_notMult5 = [num for num in range(2000, 3201) if num%7 == 0 and num%5 != 0]
div7_notMult5_test = [num for num in range(40) if num%7 == 0 and num%5 != 0]
print(div7_notMult5_test)

# Question: 2) Factorial
def myfactorial(num):
    result = 1
    for x in range(1, num+1):
        result = result*x
    return result
    
def myfact_NumList(numlist):
    temp_list = []
    if isinstance(numlist, list):
        temp_list = numlist
    else:
        temp_list.append(numlist)

    print("Factorial of a list of numbers: {}".format(temp_list))
    result = [myfactorial(x) for x in temp_list]
    print("Factorial result: {}".format(result))

myfact_NumList([4, 6, 8])