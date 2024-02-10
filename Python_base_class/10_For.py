dict = {
    '1':'11',
    '2':'22',
    '3':'33',
    '4':'44',
    '5':'55'
}

for key, value in dict.items():
    print(key, value)

# 1~10求和
sum = 0
for i in range(1, 11):#左闭右开区间
    print(i)
    sum = sum + i

print(sum)