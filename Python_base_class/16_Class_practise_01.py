# 类继承练习:人力系统
# -员工分为两类:全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
# 全职和兼职都有"姓名 name"、"工号 id"属性,都具备"打印信息 print_info"(打印姓名、工号)方法。
# 全职有"月薪 monthly_salary"属性，
# 兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性。
# 全职和兼职都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样。

# 员工类
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"Name: {self.name}, ID: {self.id}")


# 全职员工类
class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
    
    # 设置月薪
    def set_salary(self, monthly_salary):
        self.monthly_salary = monthly_salary

    # 计算月薪
    def calculate_monthly_pay(self):
        return self.monthly_salary

    # 打印月薪
    def print_salary(self):
        print(f"Monthly Salary: {self.calculate_monthly_pay()}")


# 兼职员工类  
class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    # 设置日薪
    def set_salary(self, daily_salary):
        self.daily_salary = daily_salary

    # 计算月薪
    def calculate_monthly_pay(self, work_days):
        return self.daily_salary * work_days

    # 打印月薪
    def print_salary(self):
        if self.work_days <= 0:
            print("Work days must be greater than 0.")
        else:
            print(f"Daliy Salary: {self.calculate_monthly_pay(self.work_days)}")
    

# 调试部分
employee1 = FullTimeEmployee("Alice", "F456", 5000)
employee2 = PartTimeEmployee("Bob", "P789", 100, 20000)

employee1.set_salary(6000)
employee2.set_salary(150)

employee1.print_salary()
employee2.print_salary()
    
    

    
