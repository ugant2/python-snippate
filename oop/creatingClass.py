class Student:
    def __init__(self,name,age,roll):
        if(validate(name,age,roll)):
            print("pass")
            self.__name=name
            self.__age=age
            self.__roll=roll

    def getName(self):
            return self.__name

    def getAge(self):
            return self.__age

    def getRoll(self):
            return self.__roll

    def __str__(self):
        return "name::"+self.__name +"\n age::"+str(self.__age)+"\n roll::"+str(self.__roll)

def validate(__name,__age,__roll):
    if(type(__name)==str and type(__age)==int and type(__roll)==int):
        return True
    else:
        raise Exception("type error")


s1 = Student("ram",12,23)

print(s1)

