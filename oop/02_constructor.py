class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary 
        self.name = name 
        self.bond = bond 

    def get_salary(self):
        return self.salary
    
    def get_details(self):
        print(f"Employee name: {self.name} \nSalary: {self.salary} \nBond duration: {self.bond}")
    
e1 = Employee(50000, 'john doe', 2)
e2 = Employee(40000, 'alice', 1)

print(e1.get_salary())
print(e1.name)
print()

e1.get_details()
print()
e2.get_details()