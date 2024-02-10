#定义一个学生类
# 要求:
# 1.属性包括学生姓名、学号，以及语数英三科的成绩
# 2.能够设置学生某科目的成绩
# 3.能够打印出该学生的所有科目成绩

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = {'语文': 0, '数学': 0, '英语': 0}

    def set_score(self, subject, score):
        if subject in self.scores:
            self.scores[subject] = score
        else:
            print("无效的科目")

    def print_score(self):
        print(f"{self.name}的成绩单：")
        for subject, score in self.scores.items():
            print(f"{subject}: {score}")
# 创建一个学生对象
student1 = Student("张三", "2021001")
student2 = Student("李四", "2021002")
# 设置学生的成绩
student1.set_score('语文', 85)
student1.set_score('数学', 92)
student1.set_score('英语', 78)

student2.set_score('语文', 90)
student2.set_score('数学', 88)
student2.set_score('英语', 95)

# 打印学生的成绩单      
student1.print_score()
student2.print_score()