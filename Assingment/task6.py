


#Question2... 5. Write a filter that accepts name and marks of students as dictionary and return
# only​ ​ those​ ​ who​ ​ have​ ​ passed(i.e​ ​ marks​ ​ greater​ ​ than​ ​ 40).

student = {}
def result():
    count = 0
    while count < 3:
        name = input("enter your name: ")
        mark = int(input("enter your marks: "))
        student["name"] = name
        student["marks"] = mark
        for i in student:

            if mark >= 40:
                print("pass")
            else:
                print("fail")

            return student
    count += 1

print(result())



# store all name and marks
# dictionary = {}
#
# count = 0
#
# while count < 2:
#       name = input("Enter your name: ")
#       mark = input("Enter your mark out of 100: ")
#       if name not in dictionary:
#           dictionary[name] = mark
#           count = count + 1
#
# print (dictionary)


