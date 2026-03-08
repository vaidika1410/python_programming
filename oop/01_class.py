class Employee:
    company = "Exia"

    def get_salary(self): # self refers to the object of class
        print(self)
        return 54000
    
# here self becomes e
e = Employee() # an object of class Employee is created here
print(e.get_salary()) # method of Employee is called using its object
print(e.company)