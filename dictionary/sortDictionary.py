import operator

d = {1:2, 3:4, 4:3, 2:1, 0:0}

print('original dictionery: ',d)
print("\n")

sorted_d = sorted(d.items(), key = operator.itemgetter(0))
print('Dictionary in ascending order by value: ', sorted_d)