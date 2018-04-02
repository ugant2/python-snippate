

# use of map to convert temperature celcius to faeehneight

temps = [("Berlin", 23), ("Nepal", 45), ("turkey", 22)]

c_to_f = lambda data: (data[0], (9/5)*data[1]+ 32)
print(list(map(c_to_f, temps)))

