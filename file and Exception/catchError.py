

#catching errors

f = open("myfile", "w")
f.write("hello there, my text file.\n thank you")
f.close()
try:
    file = open("myfile", "r")
    file.readline()
    file.close()
except IOError:
    print("the file doesnot exist")



try:
    f1 = open("myfile", "r")
    f1.readline()
    f1.close()
except IOError:
    print("file does not exist. Check the file")





