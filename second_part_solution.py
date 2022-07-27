class Company:
    """Outer Class"""

    company_employees = {}
    company_departments = {}

    def __init__(self, name):
        self.company_name = name

    def __str__(self):
        return f'{self.company_name}'


    def create_employee(self, first_name, last_name, age, job, salary):
        self.company_employees[f'{first_name}_{last_name}'] = \
            self.Employee(first_name, last_name, age, job, salary)

    def remove_employee(self, first_name, last_name):
        self.company_employees.pop(
            f'{first_name}_{last_name}',
            f'There is no such an employee in {self.company_name} company.'
        )

    def create_department(self, name):
        self.company_departments[f'{name}'] = self.Department(name)

    def remove_department(self, name):
        self.company_departments.pop(name, 'There is no such a department.')

    def display_departments(self):
        [print(department_name) for department_name in self.company_departments.keys()]


    # Employer as part of company Fields
    class Employee:
        """Inner Class"""

        def __init__(
            self, first_name, last_name, age, job, salary
        ):
            self.first_name: str = first_name
            self.last_name: str = last_name
            self.age: int = age
            self.job: str = job
            self.salary: int = salary
            self.bonus = 0
            self.total_salary = self.salary + self.bonus

        def __str__(self):
            return (f'Hi! My name is {self.first_name}\n'
                    f'I am an Employee of the Field company.\nMy data:\n'
                    f'  Name: {self.first_name} {self.last_name}\n'
                    f'  Age: {self.age}\n'
                    f'  Job: {self.job}\n'
                    f'  Salary: {self.salary}\n'
                    f'  Bonus: {self.bonus}\n'
                    f'  Total salary: {self.total_salary}\n')


        def apply_bonus(self, ammount):
            self.bonus += ammount
            self.total_salary += ammount

        def export_employee(self):
            ### 3 Advanced (Optional)
            with open('employee_data.txt', 'w') as file:
                file.write(
                    f'First name: {self.first_name}\n'
                    f'Last name: {self.last_name}\n'
                    f'Age: {self.age}\n'
                    f'Job: {self.job}\n'
                    f'Salary: {self.salary}\n'
                    f'Bonus: {self.bonus}\n'
                    f'Total salary: {self.total_salary}\n'
                )


    # Department as a part of company Fields
    class Department:
        """Inner Class"""

        def __init__(self, name):
            self.name: str = name
            self.department_employees = {}

        def __str__(self):
            return f'{self.name} - department of the company'


        def display_department(self):
            return self.name

        def display_employees(self):
            [print(' '.join(employee.split('_'))) for employee in self.department_employees.keys()]

        def add_employee(self, first_name, last_name):
            self.department_employees[f'{first_name}_{last_name}'] = Company.company_employees[f'{first_name}_{last_name}']

        def remove_employee(self, first_name, last_name):
            self.department_employees.pop(
                f'{first_name}_{last_name}', 
                f'There is no such an employee in {self.name} department.'
            )

        def bonus_for_everyone(self, bonus_ammount):
            for employee in self.department_employees.values():
                employee.apply_bonus(bonus_ammount)
                employee.total_salary += bonus_ammount

        def search_for_an_employee(self, first_name_or_last_name):
            ### 3 Advanced (Optional)
            for employee_name, employee_obj in self.department_employees.items():
                employee_name = employee_name.split('_')
                if first_name_or_last_name in employee_name:
                    return employee_obj
            return (f'There is no such an employee named {first_name_or_last_name} '
                    f'in {self.name} department.')



fields = Company(name='Fields')
fields.create_employee('David', 'Smith', 44, 'manager', 20000)
warehouse = fields.Department('Warehouse')
fields.create_department('Agricultural machinery')
# print(fields.company_employees)
fields.display_departments()

warehouse.add_employee(first_name='David', last_name='Smith',)

# warehouse.display_employees()


### 3 Advanced (Optional) -- searching for an Employee
david = warehouse.search_for_an_employee(first_name_or_last_name='David')
print(david)

### 3 Advanced (Optional) -- saves Employee data to a txt file in current working dir
david.export_employee()
