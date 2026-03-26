class Department:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        return f"Department : {self.name}"

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_departments(self):
        print(f"Departments in {self.name} University : ")

        for department in self.departments:
            print(department.display_info())

department1 = Department("Computer Science")
department2 = Department("Electrical Engineering")
department3 = Department("Mechanical Engineering")

university1 = University("Tech")

university1.add_department(department1)
university1.add_department(department2)
university1.add_department(department3)

university1.display_departments()
