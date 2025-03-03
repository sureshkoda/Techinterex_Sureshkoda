import os
from employee import Employee

# File to store employee data
EMPLOYEE_FILE = "employee_data.txt"

# Function to load employees from file
def load_employees():
    employees = []
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "r") as file:
            for line in file:
                data = line.strip().split(",")
                employee = Employee(
                    id=int(data[0]),
                    name=data[1],
                    position=data[2],
                    basic_salary=float(data[3]),
                    hours_worked=float(data[4]),
                    hourly_rate=float(data[5])
                )
                employees.append(employee)
    return employees

# Function to save employees to file
def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as file:
        for employee in employees:
            file.write(f"{employee.id},{employee.name},{employee.position},{employee.basic_salary},{employee.hours_worked},{employee.hourly_rate}\n")

# Function to add a new employee
def add_employee(employees):
    id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    basic_salary = float(input("Enter Basic Salary: "))
    hours_worked = float(input("Enter Hours Worked: "))
    hourly_rate = float(input("Enter Hourly Rate: "))

    employee = Employee(id, name, position, basic_salary, hours_worked, hourly_rate)
    employees.append(employee)
    save_employees(employees)
    print("Employee added successfully!")

# Function to update employee details
def update_employee(employees):
    id = int(input("Enter Employee ID to update: "))
    for employee in employees:
        if employee.id == id:
            name = input(f"Enter new name (current: {employee.name}): ") or employee.name
            position = input(f"Enter new position (current: {employee.position}): ") or employee.position
            basic_salary = float(input(f"Enter new basic salary (current: {employee.basic_salary}): ") or employee.basic_salary)
            hours_worked = float(input(f"Enter new hours worked (current: {employee.hours_worked}): ") or employee.hours_worked)
            hourly_rate = float(input(f"Enter new hourly rate (current: {employee.hourly_rate}): ") or employee.hourly_rate)

            employee.update_details(name, position, basic_salary, hours_worked, hourly_rate)
            save_employees(employees)
            print("Employee details updated successfully!")
            return
    print("Employee not found!")

# Function to delete an employee
def delete_employee(employees):
    id = int(input("Enter Employee ID to delete: "))
    for employee in employees:
        if employee.id == id:
            employees.remove(employee)
            save_employees(employees)
            print("Employee deleted successfully!")
            return
    print("Employee not found!")

# Function to view all employees
def view_employees(employees):
    if not employees:
        print("No employees found!")
    else:
        for employee in employees:
            employee.display_details()
            print("-" * 30)

# Function to calculate salary and generate payslip
def generate_payslip(employees):
    id = int(input("Enter Employee ID to generate payslip: "))
    for employee in employees:
        if employee.id == id:
            salary = employee.calculate_salary()
            print("\n--- Payslip ---")
            print(f"Employee ID: {employee.id}")
            print(f"Employee Name: {employee.name}")
            print(f"Position: {employee.position}")
            print(f"Basic Salary: {employee.basic_salary}")
            print(f"Hours Worked: {employee.hours_worked}")
            print(f"Hourly Rate: {employee.hourly_rate}")
            print(f"Total Salary: {salary}")
            print("---------------")
            return
    print("Employee not found!")

# Function to generate payroll report
def generate_payroll_report(employees):
    if not employees:
        print("No employees found!")
    else:
        total_salary = 0
        for employee in employees:
            total_salary += employee.calculate_salary()
        average_salary = total_salary / len(employees)
        print("\n--- Payroll Report ---")
        print(f"Total Employees: {len(employees)}")
        print(f"Total Salary: {total_salary}")
        print(f"Average Salary: {average_salary}")
        print("---------------------")

# Main function to run the program
def main():
    employees = load_employees()

    while True:
        print("\nEmployee Payroll System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View Employees")
        print("5. Generate Payslip")
        print("6. Generate Payroll Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            update_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            view_employees(employees)
        elif choice == "5":
            generate_payslip(employees)
        elif choice == "6":
            generate_payroll_report(employees)
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()