with open('./Txt/test.txt', 'w', encoding='utf-8') as file:
    file.write('')


with open('./Txt/test.txt', 'r+', encoding='utf-8') as f:
    print(f.read())
    f.write('床前明月光\n')
    f.write('疑是地上霜\n')
    f.write('举头望明月\n')
    f.write('低头思故乡\n')
