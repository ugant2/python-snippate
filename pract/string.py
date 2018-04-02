# Write a Python function to get a string made of the first 2
# and the last 2 chars from a given a string. If the string
# length is less than 2, return instead of the empty string.

def string_end(s):
    if len(s)<2:
        return ' '

    return len(s[0:2]) + len(s[-2:])

print(string_end('laugh out'))



# Write a Python program to change a given string to a new string
#  where the first and last chars have been exchanged.

# def change_string(s):
#
#     for i in s:
#         d = s[0:2]
#         e = s[:-2]
#         c = e + d
#         return c
#
# print(change_string("Austrlia"))
def change_string(s):
    return s[-1:] + s[1:2] + s[-2:-1] + s[:1]
print(change_string("abcd"))

#using lambda function
r = lambda s: s[-1:] + s[1:2] + s[-2:-1] + s[:1]
print(r("this"))

print("\n")

# Write a Python program to remove the characters which have odd index values of a given string


def remove_odd_char(c):
    result = " "
    for i in range(len(c)):
        if i%2 == 0:
            result += c[i]
    return result

print(remove_odd_char("bcdef"))

print("\n")

# Write a Python script that takes input from the user and
# displays that input back in upper and lower cases.
def upperLower(t):
    f = input("enter string: ")
    return f.upper()*2, f.lower()
    #return t.upper(), t.lower()
result = upperLower(2)
print(result)

#print(upperLower("can ydou discover mystery in book..."))

#using lambda function
upperLowerCase = lambda c: (c.upper(), c.lower())
print(upperLowerCase("i shoot for the moon but i am too busy gazin stars"))
print(upperLowerCase("udai lagyo panxi(bird) ley nadi tira, dana deya dhana ghatdina vancan bhakta kabira"))

