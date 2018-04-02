
# continously create a file in the Dektop
import os
i = 0
while i < 1:
    f = open("/home/ugantx/Desktop/hey.txt", "w")
    f.write("hello \n there")
    os.remove("/home/ugantx/Desktop/hey.txt")


