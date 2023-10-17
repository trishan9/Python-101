class Employee:
    no_of_employees = 0
    company_name = "Google"
    salary = "$99999"

    def __init__(self, name):
        Employee.no_of_employees += 1
        self.name = name
        self.post = "Frontend Developer"

    @property
    def employee_details(self):
        return f"{self.name} from {self.company_name} with salary {Employee.salary} is in the post of {self.post} and no of employees: {Employee.no_of_employees}"

    @staticmethod
    def change_salary(new_salary):
        Employee.salary = new_salary


e1 = Employee("Trishan Wagle")
e1.company_name = "Apple"
e1.salary = "0"
print(e1.employee_details)

Employee.change_salary("00000")

e2 = Employee("Giga Chad")
print(e2.employee_details)

e3 = Employee("John Doe")
print(e3.employee_details)
