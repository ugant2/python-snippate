



#Question2 3. Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number. (Hint: split
# function)

import time

def split_list_tuple():

    start_time = time.clock()
    print("{}".format(start_time))

    data = input("enter the number:")
    list = data.split(",")
    print("list: ", list)
    print("tuple: ", tuple(list))


    final_time = time.clock() - start_time
    print("{}".format(final_time))

print(str(split_list_tuple()))