

class Employee:

    #constructor or initializer
    def __init__(self, firstName, lastName, pay, email):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = email

    # method in the class that prints last name, first name and email
    def name(self):
        return '{}{}{}{}'.format(self.firstName, self.lastName,  self.pay, self.email)

    def __str__(self):
        return "first Name::"+self.firstName + " " + "Last Name::" + self.lastName + "Pay::"+str(self.pay)+" "+"Email::"+self.email

# creating object
emp_1 = Employee("Test", "User", 7000, "test@mail.com")


print(emp_1)

