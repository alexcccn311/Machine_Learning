# 数值对象
a = 10
print(type(a))  # <class 'int'>  # 整数（int）

b = 3.14
print(type(b))  # <class 'float'>  # 浮点数（float）

c = 2 + 3j
print(type(c))  # <class 'complex'>  # 复数（complex）

# 序列对象

d = "Hello, World!"
print(type(d))  # <class 'str'>  # 字符串（str）

e = [1, 2, 3]
print(type(e))  # <class 'list'>  # 列表（list）

f = (1, 2, 3)
print(type(f))  # <class 'tuple'>  # 元组（tuple）

g = range(10) #从0-9，range函数默认从0开始，到x-1结束。
print(type(g))  # <class 'range'>  # 范围（range）

# 映射对象
h = {"name": "Alice", "age": 25}
print(type(h))  # <class 'dict'>  # 字典（dict）

# 集合对象

i = {1, 2, 3}
print(type(i))  # <class 'set'>  # 集合（set）

j = frozenset([1, 2, 3, 4, 5])
print(type(j))  # <class 'frozenset'>  # 冻结集合（frozenset）

# 布尔对象
k = True
print(type(k))  # <class 'bool'>  # 布尔值（bool）

# 特殊对象

l = None
print(type(l))  # <class 'NoneType'>  # 空值（NoneType）

m = b"Hello"
print(type(m))  # <class 'bytes'>  # 字节（bytes）

n = bytearray(5)
print(type(n))  # <class 'bytearray'>  # 字节数组（bytearray）

o = memoryview(b"Hello")
print(type(o))  # <class 'memoryview'>  # 内存视图（memoryview）

# 可调用对象
def my_function():
    pass

print(type(my_function))  # <class 'function'>  # 函数（function）

class MyClass:
    def method(self):
        pass

obj = MyClass()
print(type(obj.method))  # <class 'method'>  # 方法（method）
print(type(MyClass))     # <class 'type'>  # 类（class）
print(type(obj))         # <class '__main__.MyClass'>  # 类的实例（instance of class）

# 模块和包
import math
print(type(math))  # <class 'module'>  # 模块（module）