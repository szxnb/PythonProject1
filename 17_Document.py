# 打开一个文件
file = open("./Txt/hello.txt", "r", encoding="utf-8")
# 读取文件内容
content = file.read()
# 关闭文件
file.close()

print(content)

print("---------------------")

with open("./Txt/hello.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("---------------------")

with open("./Txt/hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
        