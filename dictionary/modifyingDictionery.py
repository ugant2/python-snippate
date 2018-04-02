d2 = {"spam":2, "ham":1, "eggs":3}
print(d2,"\t")

print("\t")

#change entry
d2["ham"] = ["grill", "bake", "fry"]
print(d2)

print("\t")

del d2["eggs"]  #delete entry based on keyword
print(d2)

print("\t")

d2["brunch"] = "bacon"  #add new entry
print(d2)