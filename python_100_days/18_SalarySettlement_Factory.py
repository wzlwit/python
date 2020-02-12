# manager: 15000/m ; programmer: 200/h ; saler: 1800/m + commissionary: 5%
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000.0


class Programmer(Employee):

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():

    @staticmethod
    def create(emp_type, *args, **kwargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp


def main():
    emps = [
        EmployeeFactory.create('M', 'CaoCao'),
        EmployeeFactory.create('P', 'XunYu', 120),
        EmployeeFactory.create('P', 'GuoJIa', 85),
        EmployeeFactory.create('S', 'DianWei', 123000),
    ]
    for emp in emps:
        print('%s: %.2fYuan' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
