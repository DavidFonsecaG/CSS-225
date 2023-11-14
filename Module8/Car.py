
class Employee:
    # Constructor method
    def __init__(self, name, pay):
        self.name = name
        self.email = name + "@mycompany.ai"
        self.pay = pay

    # Method to get pay
    def get_pay(self):
        return self.pay

    def request_raise(self):
        if self.pay < 30:
            return f"Sr. boss I am currently making {self.pay}, and I want to make triple than that!"
        else:
            return f"Sr. boss I am currently making {self.pay}, and I want to make double than that!"


emp_1 = Employee("David", 7)

print(emp_1.request_raise())



