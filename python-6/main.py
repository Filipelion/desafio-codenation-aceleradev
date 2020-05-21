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
        self._departament = Department('managers', 1)


    def calc_bonus(self):
        return self.salary * 0.15

    #@property
    def get_department(self):
        return self._departament.name

    def set_department(self, name):
        self._departament.name = name


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__sales = 0

    #@property
    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value

    def calc_bonus(self):
        return self.__sales * 0.15

