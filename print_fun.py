# 作 者：田宗林
# 时 间：2021/7/11
# print函数 ->输出
"""
内容：
    1. 数字
    2. 字符串
    3. 含有运算符的表达式
目的地
    1. 显示器
    2. 文件
形式：
    1. 换行
    2. 不换行
"""
print(520)
print(3 + 1)

# 将数据输出到文件中
#   1. 指定盘符→E:/Programs/file_name
#   2. 指定关键字形参file=

fp = open('../T_files/print.txt', 'a+')
print('Hello world', file=fp)

# 同行输出
print('hello', 'python')