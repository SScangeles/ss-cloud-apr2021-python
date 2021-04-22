
# 1) Print 'r' from 'Hello World'
print("Hello World"[8])

# 2) String slicing
print("thinker"[2:-2])

# 3) Sammy
s = "Sammy"
print(s[2:])

# 4) Mississippi to distinct character word
print("".join(set("Mississippi")))

import string
def palindrome(input):
    result = []
    exclude = set(string.punctuation)
    print("Panlindrome check:\n{}".format(input))
    for word in input:
        temp = word
        if len(word) > 1:
            temp = "".join("".join(x for x in word if x not in exclude).split()).lower()
            if temp[::-1] == temp:
                result.append("Y")
            else:
                result.append("N")
        
    return print(result)

# 5) Palindrome ignore punctuations, single characters
palindrome(["H, an, nah!!", "def not a palin"])
