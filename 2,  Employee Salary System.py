class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def increase_salary(self, amount):
        self.salary += amount
        print("Salary increased successfully.")
    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
emp1 = Employee("Abhiraj", 101, 25000)
emp1.display_details()
emp1.increase_salary(5000)
emp1.display_details()