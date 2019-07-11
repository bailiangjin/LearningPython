

import re

def hump2underline(hunp_str):
    '''
    驼峰形式字符串转成下划线形式
    :param hunp_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    '''
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 这里第二个参数使用了正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub

def underline2hump(underline_str):
    '''
    下划线形式字符串转成驼峰形式
    :param underline_str: 下划线形式字符串
    :return: 驼峰形式字符串
    '''
    # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
    sub = re.sub(r'(_\w)',lambda x:x.group(1)[1].upper(),underline_str)
    sub = "@SerializedName(\""+underline_str+"\")\n"+ sub
    return sub

print(hump2underline("subName"))

print(underline2hump("sub_name"))

# sourceFile = open('code.txt')
# code_content = sourceFile.read()  # Read file content
# print(code_content)
# humpContent=underline2hump(code_content)
# print(humpContent)
#
# aimedFile = open('code_new.txt','w')  # Open file to write
# aimedFile.write(humpContent)

sourceFile = open('code.txt')
aimedFile = open('code_new.txt', 'w')
result = list()
for line in sourceFile.readlines():                          #依次读取每行
    line = line.strip()                             #去掉每行头尾空白
    if not len(line) or line.startswith('#'):       #判断是否是空行或注释行
        continue                                    #是的话，跳过不处理
    result.append(underline2hump(line))                             #保存
    aimedFile.write(underline2hump(line)+"\n")
