from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC, Department):

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_department(self):
        return self.__departament.name

    def set_department(self, name):
        self.__departament.name = name


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.department = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value

    def get_department(self):
        return self.department.name

    def set_department(self, name):
        self.department.name = name
