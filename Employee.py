class Employee:
    def __init__(self,first_name,last_name,employee_ID):
        self.first_name=first_name
        self.last_name=last_name
        self.employee_ID=employee_ID
        self.base_salary=0
    def set_base_salary(self,value):
        value=self.base_salary
        return value
class TeachingStaff(Employee):
    def __init__(self,first_name,last_name,employee_ID,teaching_area,category):
        super().__init__(first_name,last_name,employee_ID)
        self.teaching_area=teaching_area
        if 1<self.category<=5:
            self.category=category
    def get_salary(self):
        result=(((self.category*10)+100)/100)*self.base_salary
        return result
    def get_staff_info(self):
        print(f"First Name:{self.first_name}\nLast Name:{self.last_name}\nEmployee ID:{self.employee_ID},Teaching:{self.teaching_area}\nCategory:{self.category}\nSalary:{self.get_salary()}")
        
class AdministrativeStaff(Employee):
    def __init__(self,first_name,last_name,employee_ID,level):
        super().__init__(first_name,last_name,employee_ID)
        if 1<self.level<=3:
            self.level
    def get_salary(self):
        result=((self.level*15)+100)/100*self.base_salary
        return result
    def get_staff_info(self):
        print(f"First Name:{self.first_name}\nLast Name:{self.last_name}\nEmployee ID:{self.employee_ID}\nTeaching:{self.teaching}\Category:{self.category}\hSalary:{self.get_salary()}")
jerry=TeachingStaff("Jerry","Smith",110022123,"IT",3)
jerry.set_base_salary(90000)
print(jerry.get_staff_info())
