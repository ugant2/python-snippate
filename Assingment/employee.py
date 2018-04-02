

class Employee:

    def __init__(self, name, dob, join_date, salary):
        self.name = name
        self.dob = dob
        self.join_date = join_date
        self.salary = salary

    def addRecord(self):
        print("record added")

    def deleteRecord(self):
        print("record deleted")


class Developer(Employee):
    def __init__(self, name, dob, doj, salary, pro_lang):
        super().__init__(name, dob, doj, salary)
        self.pro_lang = pro_lang

    def addRecord(self):
        try:
            name = input("Name: ")
            dob = str(input("Date of Birth: "))
            doj = str(input("Date of Joined: "))
            salary = str(input("Salary: "))
            pro_lang = str(input("Programing language: "))
            f = open("empolyee", "w")
            f.write("Name: {0}| DoB:{1}| DoJoined:{2}| Salary:{3}| Programmng Language:{4}".format(name, dob, doj, salary, pro_lang))

            return "Name:"+ name+ "|" + "DoB:"+ dob + "Salary:"+ salary + "Progaming Language:"+ pro_lang
            print("\n")

        except TypeError:
            print("input corrrect data type")
        finally:
            f.close()


class Hr(Employee):
    def __init__(self, name, dob, doj, salary, training):
        super().__init__(name, dob, doj, salary)
        self.training = training

    def addRecord(self):
        try:
            name = input("Name: ")
            dob = str(input("Date of Birth: "))
            doj = str(input("Date of Joined: "))
            salary = str(input("Salary: "))
            training = str(input("Training: "))
            f = open("empolyee", "w")
            f.write()
        except TypeError:
            print("input corrrect data type")
        finally:
            f.close()


emp1 = Developer('1', '3', '4', '5', '5')
print(emp1.addRecord())






















