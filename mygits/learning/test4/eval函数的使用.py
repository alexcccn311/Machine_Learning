#eval函数主要用来去掉字符串的引号，将字符串直接转换为数值#
s='3.1415926'
b='3.14+3'
print(eval(s),type((s)),type(eval(s)))
print(eval(b),type((b)),type(eval(b)))

#eval函数常与input一起使用,方便直接调用进行运算。
a=input('你的年龄：')
age = eval(a)
print('6年后你将',age+6,'岁。',sep='')
print('6年后你将',int(a)+6,'岁。',sep='')

#除了去除数字的引号，还可以用作去除文本的引号

a='求你肏我'
print(a)
try:
    print(eval('求你肏我'))
except (SyntaxError, NameError):
    print("无法使用 eval 解析非 Python 表达式的字符串")