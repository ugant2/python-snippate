#use of filter function

countries = ["Nepal", "", "", "India", "China", "", "Spain", "", "USA", "Chile"]
print(list(filter(None, countries)))


number  = [2,4,5,6,7,3,6,11,16]
print(list(filter(lambda n: n%2==0, number)))