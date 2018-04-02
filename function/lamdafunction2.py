

# combine first name and last name into single "full name"

full_name = lambda fn, ln: fn.split() + ln.split()
print(full_name("yufanr", "the"))



#lambda function to sort alphabetically

authors = ["paulo cohelo", "mark twin", "robbin sharma", "laxmi parsad devkota","madhav parsad gmere"]
authors.sort(key=lambda name: name.split())
print(authors)

print("\n")
#quardratic functions f(x)=ax^2 + bx + c
def build_quardratic_function(a,b,c):
    return lambda x: a*x**2 + b*x + c


print(build_quardratic_function(4,5,6)(2))