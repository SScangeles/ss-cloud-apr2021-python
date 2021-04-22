
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
    exclude = set(string.punctuation)
    result = []
    temp_list = []

    if isinstance(input, list):
        temp_list = input
    else:
        temp_list.append(input)
        
    print("Panlindrome check:\n{}".format(input))
    for word in temp_list:
        temp = word
        if len(word) > 1:
            temp = "".join("".join(x for x in word if x not in exclude).split()).lower()
            if temp[::-1] == temp:
                result.append("Y")
            else:
                result.append("N")
        
    return print(result)

# 5) Palindrome ignore punctuations, single characters
palindrome("H, an, nah!!")
