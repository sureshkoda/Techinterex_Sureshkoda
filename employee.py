class Employee:
    def __init__(self, id, name, position, basic_salary, hours_worked, hourly_rate):
        self.id = id
        self.name = name
        self.position = position
        self.basic_salary = basic_salary
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def display_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Hourly Rate: {self.hourly_rate}")

    def calculate_salary(self):
        return self.basic_salary + (self.hourly_rate * self.hours_worked)

    def update_details(self, name=None, position=None, basic_salary=None, hours_worked=None, hourly_rate=None):
        if name:
            self.name = name
        if position:
            self.position = position
        if basic_salary:
            self.basic_salary = basic_salary
        if hours_worked:
            self.hours_worked = hours_worked
        if hourly_rate:
            self.hourly_rate = hourly_rate