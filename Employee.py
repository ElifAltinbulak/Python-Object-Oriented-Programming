"""Task 1 Create the Employee class with the following requirements: 
•first_name – attribute to hold the first name of the employee 
•last_name – attribute  to hold the last name of the employee  
• employee_ID – attribute to hold the ID number of the employee 
• base_salary – this attribute is not provided by the user when the class is initialised. 
It is set to 0 in the init function. The method set_base_salary() can be used to set a base salary. 
• set_base_salary() – This method takes one input and sets the value of the base_salary attribute.

Task 2 (10 marks) Create the Teaching Staff class with the following requirements: 
• teaching_area – string capturing the academic area this staff member teaches,
e.g., “programming” • category – an integer between 1 and 5 (inclusive) that can be used to determine the level of this staff member. 
• getsalary() – this calculates the salary of the staff member using their category and the base salary. The formula for calculating the salary is:  
𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 =(𝑐𝑐𝑠𝑠𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑠𝑠𝑠𝑠 ∗10)  + 100100 ∗𝑏𝑏𝑠𝑠𝑠𝑠𝑐𝑐𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠  
• get_staff_info – should return the details of the staff member including their salaries

Create the Administrative Staff class with the following requirements: 
• Level – an integer between 1 and 3 (inclusive) that can be used to determine the level of this staff member 
• getsalary() – this calculates the salary of the staff member using their level and the base salary. The formula for calculating the salary is:  
𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 =(𝑠𝑠𝑐𝑐𝑙𝑙𝑐𝑐𝑠𝑠 ∗15) + 100100 ∗𝑏𝑏𝑠𝑠𝑠𝑠𝑐𝑐𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 
• get_staff_info: should return the details of the staff member including their salaries
"""



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
