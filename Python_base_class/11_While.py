is_done = False
sum = 0
i = 0

user_input_num = input("please input a number:")
while user_input_num != "q":
    sum += int(user_input_num)
    i += 1
    user_input_num = input("please input a number:")

if i == 0:
    pass
else:
    print("average = " + str(sum / i))
