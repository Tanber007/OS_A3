# Simple Employee Salary Management System
# Demonstrates Python Functions, Parameters, Return Statements, and File Handling

FILE_NAME = "employees.txt"


def format_employee_record(name, emp_id, salary):
    """Formats employee details into a single pipe-separated line."""
    return f"{name} | {emp_id} | {salary}\n"


def get_employee_input():
    """Collects and returns employee details from the user."""
    name = input("Enter Name: ").strip()
    emp_id = input("Enter ID: ").strip()

    # Validate that salary is a valid number
    while True:
        salary_input = input("Enter Salary: ").strip()
        if salary_input.replace(".", "", 1).isdigit():
            salary = int(salary_input) if salary_input.isdigit() else float(salary_input)
            break
        print("Invalid input. Please enter a numeric value for Salary.")

    return name, emp_id, salary


def add_employee(name, emp_id, salary):
    """Appends a formatted employee record to employees.txt and returns a status message."""
    record = format_employee_record(name, emp_id, salary)
    with open(FILE_NAME, "a") as file:
        file.write(record)
    return "Employee Added Successfully"


def view_employees():
    """Reads all records from employees.txt and returns them as a list of strings."""
    try:
        with open(FILE_NAME, "r") as file:
            records = [line.strip() for line in file if line.strip()]
        return records
    except FileNotFoundError:
        return []


def display_menu():
    """Prints the main menu options."""
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")


def main():
    """Controls the main program loop."""
    while True:
        display_menu()
        choice = input("Choose Option: ").strip()

        if choice == "1":
            name, emp_id, salary = get_employee_input()
            status = add_employee(name, emp_id, salary)
            print(status)

        elif choice == "2":
            records = view_employees()
            if not records:
                print("No employee records found.")
            else:
                print("\n--- Employee Records ---")
                for record in records:
                    print(record)

        elif choice == "3":
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()