class Employee:
    """Common base class for all employees"""
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee {}".format(Employee.empCount))

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

# This would create first object of Employee class"
emp1 = Employee("Tim", 200000)
emp1.displayCount()
emp1.displayEmployee()
# This would create second object of Employee class"
emp2 = Employee("Bob", 5000)
Employee.newvar = 10 # Add "newvar" class variable to Employee class
emp2.displayCount()
emp2.displayEmployee()