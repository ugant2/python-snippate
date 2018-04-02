

# Question​ ​ 2 1. Define a function that computes the length of a given list or string(Do not use
# library​ ​ function​ ​ of​ ​ length).


def count_length_list(): #function without any parameter
    c = 0
    l = [3,4,5,6,7,78,2]
    for i in l:
        c = c + 1
    return c
print(count_length_list(), "\n")


def count_lenght_string(): #function without any parameter
    counter = 0
    s = "ablze"
    for i in s:
        counter += 1
    return counter
print(count_lenght_string(), "\n")

def count_input_user(): #function asking for input
    counter = 0
    l = input("enter the number:")
    for i in l:
        counter += 1
    return counter
print(int(count_input_user()), "\n")

def count_input_string(): #function asking for string
    counter = 0
    l = input("enter the string:")
    for i in l:
        counter += 1
    return counter
print(count_input_string(), "\n")

def count_list(k): #function with parameter
    counter = 0
    for i in k:
        counter += 1
    return counter
print(int(count_list("123")), "\n")


def count_string(s): #function with paramater
    counter = 0
    for i in s:
        counter += 1
    return counter
print(count_string("this is"), "\n")
