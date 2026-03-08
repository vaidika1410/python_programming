class Employee:
    company = 'ASUS' # class attribute

    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company

    def get_info(self):
        print(f"Employee name: {self.name}\nSalary: {self.salary}\nCompany: {self.company}")

# e1 = Employee('Vaidika', 55000, )
e2 = Employee("Gautam", 60000, 'Nvidia')
print(e2.company)

e2.get_info()