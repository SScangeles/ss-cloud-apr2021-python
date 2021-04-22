
# Question 1:
# 1) List of ...
list1 = [1, "hello world", 3.14]
print(list1)

# 2) List of [1,1[1,2]], grab 2
list2 = [1, 1, [1,2]]
print(list2[2][1])

# 3) print list[1:]
list3 = ["a", "b", "c"]
print(list3[1:])

# 4) create dictionary and assign to var
week = {
    "sunday":1,
    "monday":2,
    "tuesday":3,
    "wednesday":4,
    "thursday":5,
    "friday":6,
    "saturday":7
}

day = week["sunday"]
print("Sunday is day:", day)

# 5) list to tuple
list5 = [1, [1,2]]
tuple5 = (list5[0], list5[1])
print(tuple5)

# 6) Mississippi to distinct character word
print("".join(set("Mississippi")))