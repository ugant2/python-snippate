

# Question​ ​ 3
# Write a program to store the stock information of a departmental store. Information
# should be name, price, quantity and type of item. Use while loop to take the input until
# user wants. You need to write those information in a file. After the use inputs data,
# display information for specific item by reading the file written in first step. Use file
# handling with proper exception handling. You may use data structures if you want.
# Please​ ​ use​ ​ delimiters​ ​ like​ ​ ; ​ ​ or​ ​ | ​ ​ to​ ​ separate​ ​ the​ ​ data​ ​ values.


try:
    i = 0
    while i < 2:
        name = input("name: ")
        price = str(input("price: "))
        quantity = str(input("quantity: "))
        type = str(input("type: "))
        f = open("department.txt", "w")
        f.write("Name:"+name +"|"+ "Price:" + price +"|"+ "Qunatity:" + quantity +"|"+ "Type:" + type)
        i += 1
        print("\n")
except TypeError:
    print("insert correct data type")
finally:
    f.close()


try:
    f1 = open("department.txt", "r")
    print(f1.read())
except IOError:
    print("file not found")
finally:
    f1.close()




