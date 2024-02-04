# mood_index = int(input("输入对象的心情指数:"))
# is_at_home = input("True or False:")
#
# print(type(bool("False")))
# print(bool(" "))
#
# if mood_index >= 50:
#     if is_at_home == "False":
#         print("可以打游戏")
#     else:
#         print("No")
# else:
#     print("不能打游戏")

height = float(input("Please input your height:"))
weight = float(input("Please input your weight:"))
bmi_index = weight / height ** 2

print("Your BMI index is : " + str(bmi_index))

if bmi_index <= 0:
    print("ERROR!")
elif bmi_index > 0 and bmi_index < 15:
    print("Too Short")
elif bmi_index >= 15 and bmi_index < 20:
    print("Health BMI index")
else:
    print("Too fat")
    