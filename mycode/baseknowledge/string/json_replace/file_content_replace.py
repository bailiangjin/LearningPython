from mycode.baseknowledge.string.string_converter import underline2hump, hump2underline


print(hump2underline("subName"))

print(underline2hump("sub_name"))


sourceFile = open('json_org.txt')
aimedFile = open('json_new.txt', 'w')
result = list()
for line in sourceFile.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
        continue  # 是的话，跳过不处理
    result.append(underline2hump(line))  # 保存
    aimedFile.write(underline2hump(line) + "\n")



sourceFile = open('json_new.txt')
aimedFile = open('json_new_to_org.txt', 'w')
result = list()
for line in sourceFile.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
        continue  # 是的话，跳过不处理
    result.append(hump2underline(line))  # 保存
    aimedFile.write(hump2underline(line) + "\n")
