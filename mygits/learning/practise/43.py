lst = ['a','b','c','d','e']
for item in lst:
    print(item)
f = len(lst)
print(f)
for i in range(0,len(lst)):
    print(i,'-->',lst[i])
for index,item in enumerate(lst,1):
    print(index,'-->',item)