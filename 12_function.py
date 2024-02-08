def bmi_func(height, weight):
    bmi_index = weight / height ** 2

    if bmi_index <= 0:
        print("ERROR!")
        return bmi_index, 'ERROR'
    elif bmi_index > 0 and bmi_index < 15:
        print("Too Short")
        return bmi_index, 'Too Short'
    elif bmi_index >= 15 and bmi_index < 20:
        print("Health BMI index")
        return bmi_index, 'Heath'
    else:
        print("Too fat")
        return bmi_index, 'Too fat'

# bmi_index1,condition1 = bmi_func(1.7, 50)
# bmi_index2,condition2 = bmi_func(1.0, 50)
# bmi_index3,condition3 = bmi_func(1.5, 50)
# print(f"{bmi_index1: .2f}",condition1)
# print(f"{bmi_index2: .2f}",condition2)
# print(f"{bmi_index3: .2f}",condition3)