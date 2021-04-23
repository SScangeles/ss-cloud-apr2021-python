
# 1) Find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
div7_notMult5 = [num for num in range(
    1500, 2701) if num % 7 == 0 and num % 5 == 0]
print(div7_notMult5)

# 2) Convert celsius to and from fahrenheit

# 3) Guess that number!

# 4) Pattern
def mypattern(n):
    for x in range(1, n+1):
        print("* "*x)
    for x in range(n-1, 0, -1):
        print("* "*x)

mypattern(5)

# 5) Reverse input
print("Enter string to reverse:")
input5 = input()
print(input5[::-1])

# 6) Count even and odd numbers

# 7) Print mixed list datatypes

# 8) Print 0-6 except 3 and 6
for x in range(7):
    if x != 3 and x != 6:
        print(x, end=" ")
print()
