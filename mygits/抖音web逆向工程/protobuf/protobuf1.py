from Protobuf3_pb2 import Person, Info

p1 = Person()    #定义数据内容#
p1.name = "John"
p1.age = 25
info = p1.SerializeToString()  #序列化数据#
print(info)      #一般这一步直接传输数据#

p2 = Info()                          #定义数据内容#
p2.method = "POST"
p2.payload = '你好。'
info = p2.SerializeToString()    #序列化数据#
print(info)       #一般这一步直接传输数据#

obj =Info()         #选取数据对象#
obj.ParseFromString(info)      #反序列化数据#
print(obj.method)                #输出数据#
print(obj.payload)

obj = Info()        #选取数据对象#
print(dir(obj))          #dir命令可以返回对象的所有属性和方法#