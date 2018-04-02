


'''Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]'''


color_list = ["Red", "Green", "White", "Black"]

#using lambda function
# color_print = lambda color: for color in color_list if color == [0] and color == [-1]
# print(color_print)

#using list comprehension
color_list_print = [color for color in color_list if color == [0] and color == [-1]] #color = paramater to be printed
print(color_list_print)


print(color_list[0],color_list[-1])

print("\n")

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014


exam_st_date = (11,12,2014)
print("the exam start from:%d %d %d"%(exam_st_date))


print("\n")

# Write a Python program that accepts an integer(n) and computes the value of n + nn + nnn.
# a = int(input("enter an integer"))
# n1 = int("%s" %(a))
# n2 = int("%s%s" %(a,a))
# n3 = int("%s%s%s" %(a,a,a))
# print("n + nn + nnn sum up is: ", n1+n2+n3)


# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(dict.__doc__)

print("\n")

# Write a Python program to print the calendar of a given month and year.
import calendar

y = int(input("enter year: "))
m = int(input("enter month: "))
print(calendar.month(y,m))

#using lambda function
da = lambda y, m: calendar.month(y, m)
print(da(4,5))

print("\n")

# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum

def sum_three(x,y,z):
    sum = x + y + z
    if x==y==z:
        sum *= 3
    return sum

print(sum_three(3,4,6))
print(sum_three(5,5,5))

# h = lambda x, y, z: x + y + z if x==y==z sum += 3

# print(h(2,3,4))
