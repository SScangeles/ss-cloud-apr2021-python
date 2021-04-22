
# 1) Print 'r' from 'Hello World'
print("Hello World"[8])

# 2) String slicing
print("thinker"[2:-2])

# 3) Sammy
s = "Sammy"
print(s[2:])

# 4) Mississippi to distinct character word
print("".join(set("Mississippi")))


def palindrome(input):
    result = input
    if len(input) > 1:
        result = "".join(("".join([x for x in input.split(",")])).split())
        if result[::-1] == result:
            return print("'{}' is a palindrome:".format(input), result)
    return print("not a palindrome:", result)


# 5) Palindrome
palindrome("h, an, nah")
