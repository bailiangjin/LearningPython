# 字符串

## 字符串合并

s1 = 'hello'

s2 = 'world'

s3 = s1 + s2

print(s1)
print(s2)
print(s3)

## 字符串切分

s = 'Spam'

### 正序
print(s[0])

### 倒序
print(s[-1])

## 分片切分

### 正序

print(s[1:3])
print(s[1:])
print(s[:3])

print(s[-3:-1])
print(s[:-1])
print(s[-1])

### 有效地拷贝一个字符串
print(s[:])

## 字符串的不可变性

## 数字、字符串、元数组是不可变的，列表和字典是可变的

### 查找 替换

print(s.find('a'))
print(s.replace('pa', "PA"))

### 分割
line = 'aaa,bbb,ccc,dd'

print(line.split(','))

### 大小写转换

str = "www.xianhuagushici.com"

print(str.upper())  # 把所有字符中的小写字母转换成大写字母
print(str.lower())  # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
print(str.title())  # 把每个单词的第一个字母转化为大写，其余小写
print(str.isalpha())  # 判断字符串是否都是字母
print(str.isalnum())  # 判断字符串是否都是字母或数字
print(str.isnumeric())  # 判断字符串是否都是数字

str = 'aabb \n'
print(str)
print(str.rstrip())  # 去除字符串里的空字符

### 格式化字符

str = '%s, eggs, and %s' % ('haha', 'heihei!')  # Formatting expression (all)
# 'spam, eggs, and SPAM!'

print(str)
str = '{0}, eggs, and {1}'.format('spam', 'SPAM!')  # Formatting method (2.6, 3.0)
# 'spam, eggs, and SPAM!'
print(str)

print(dir(str))  # 输出字符串的所有方法

length = len(dir(str))

sFuncNumberStr = "字符串公有%d个方法" % length

print(sFuncNumberStr)  # 输出字符串的所有方法

# 使用help查看某个方法的用法
print(help(str.capitalize))

### 使用反斜杠 表示字符转义

S = 'A\nB\tC'  # \n is end-of-line, \t is tab
print(len(S))  # Each stands for just one character

print(ord('\n'))  # 查询字母的ASCII码值 # \n is a byte with the binary value 10 in ASCII

S = 'A\0B\0C'  # \0, a binary zero byte, does not terminate string
print(len(S))


# 正则匹配

import re

match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')

print(match.group(1))
print(match.groups())


match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())
