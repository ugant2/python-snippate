

# Question 2 2. Write a function that takes a character (i.e. a string of length 1) and returns True
# if​ ​ it​ ​ is​ ​ a ​ ​ vowel,​ ​ False​ ​ otherwise.

def character():
    c = input("enter the string(one letter recommended): ")
    # p = [d for i in len(c) (if d == "a" and d == "e" and d == "i" and
    # d == "o" and d == "u"),(print("True"),else,print("False"))]
    for i in c:
        if i == "a" and i == "e" and i == "i" and i == "o" and i == "u":
            print("True")
    else:
            print("False")

    return c #return or print string entered by user

print(character())


