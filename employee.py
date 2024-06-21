class Employee:
    def __init__(self, employeeID, name, salary):
        self.employeeID = employeeID
        self.name = name
        self.salary = salary

    def printEmployee(self):
        print(self.employeeID, self.name, self.salary)


class Manager(Employee):
    def __init__(self, employeeID, name, salary, department, list_of_employees):
        super().__init__(employeeID, name, salary)
        self.department = department
        self.list_of_employees = list_of_employees

    def printManager(self):
        print(self.employeeID, self.name, self.salary, self.department, self.list_of_employees)


class Developers(Employee):
    def __init__(self, employeeID, name, salary, list_of_languages):
        super().__init__(employeeID, name, salary)
        self.list_of_languages = list_of_languages

    def printDevelopers(self):
        print(self.employeeID, self.name, self.salary, self.list_of_languages)


class Interns(Employee):
    def __init__(self, employeeID, name, salary, school_name, graduation_year):
        super().__init__(employeeID, name, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year

    def printInterns(self):
        print(self.employeeID, self.name, self.salary, self.school_name, self.graduation_year)

#OBJECTS

employee1 = Employee(1, "Japheth Kamau", 24000)
employee1.printEmployee()
employee2 = Employee(2, "Gideon Kamau", 12000)
employee2.printEmployee()
employee3 = Employee(3, "Leonel Messi", 12000)
employee3.printEmployee()
employee4 = Employee(4, "Gibson Doe", 12000)
employee4.printEmployee()
employee5 = Employee(5, "Neymar Junior", 12000)
employee5.printEmployee()
manager = Manager(1, "Japheth Kamau", 24000, "Finance", ["Jane", "Kate", "Julius"])
manager.printManager()
developers= Developers(1, "Mark Twain", 13000, ["Python", "Java", "Kotlin"])
developers.printDevelopers()

