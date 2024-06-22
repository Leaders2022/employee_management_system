class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, employees_managed=None):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.employees_managed = employees_managed
        if employees_managed is not None:
            self.employees_managed.display_information()
        else:
            def display_information(self):
                super().display_information()
                print(f"Department: {self.department}")
                print(f"Employees Managed: {[employee.name for employee in self.employees_managed]}")

            def add_employee(self, employee):
                self.employees_managed.append(employee)

            def display_employees_managed(self):
                print("Employees Managed: ")
                for employee in self.employees_managed:
                    print(f"{employee.name}: (ID: {employee.employee_id})")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_languages=None):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages
        if programming_languages is not None:
            self.programming_languages.display_information()
        else:
            def display_information(self):
                super().display_information()
                print(f"Programming Languages: {','.join(self.programming_languages)}")

            def add_programming_language(self, programming_language):
                if programming_language is not None:
                    self.programming_languages.append(programming_language)


class Intern(Employee):
    def __init__(self, name, employee_id, salary, school_name, graduation_year):
        super().__init__(name, employee_id, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year

    def display_information(self):
        super().display_information()
        print(f"School name: {self.school_name}")
        print(f"Graduation Year: {self.graduation_year}")


# CREATE SOME EMPLOYEES
manager = Manager("George", 1, 900000, "Software Engineeering")
developer = Developer("Keysha", 2, 100000, ["Java", "Java"])
intern = Intern("Gee", 3, 30000, "A&M University")

# DISPLAY THEIR INFORMATION
manager.display_information()
print()
developer.display_information()
print()
intern.display_information()

# MANAGER ADDS EMPLOYEES TO MANAGE
manager.add_employee(developer)
manager.add_employee(intern)

# DISPLAY THE LIST OF EMPLOYEES MANAGED BY THE MANAGER
manager.display_employees_managed()

#DEVELOPER ADDS A NEW PROGRAMMING LANGUAGE
developer.add_programming_language("Java")
developer.display_information()

#CALCULATE AND PRINT ANNUAL SALARIES
print(f"{manager.name}'s Annual Salary: Ksh{manager.calculate_annual_salary()}")
print(f"{developer.name}'s Annual Salary: Ksh{developer.calculate_annual_salary()}")
print(f"{intern.name}'s Annual Salary: Ksh{intern.calculate_annual_salary()}")



