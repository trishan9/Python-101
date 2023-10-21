class Employee:
    company_name = "Google"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    @classmethod
    def change_company(self, new_company):
        self.company_name = new_company

    def show_details(self):
        print(f"{self.name} with {self.id} is from {self.company_name}")


class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

    def show_details(self):
        super().show_details()
        print(f"His language is {self.language}")


e1 = Employee("Trishan", "1")
e1.change_company("Tesla")
print(e1.company_name)
e1.show_details()

e2 = Employee("Wagle", "2")
print(e2.company_name)

e3 = Programmer("Trishan", "2", "MERN")
print(e3.name)
print(e3.language)
e3.show_details()

print(dir(Employee))
print(e3.__dict__)
print(help(Programmer))
