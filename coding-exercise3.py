
# 1) Print 'r' from 'Hello World'
print("Hello World"[8])

# 2) String slicing
print("thinker"[2:-2])

# 3) Sammy
s = "Sammy"
print(s[2:])

# 4) Mississippi to distinct character word
# print("Mississippi"[:])

# 5) Palindrome


def palindrome(input):
    result = input
    if len(input) > 1:
        result = "".join(("".join([x for x in input.split(",")])).split())
        if result[::-1] == result:
         return print("'{}' is palindrome:".format(input), result)
    return print("not palindrome:", result)


palindrome("h, an, nah")
