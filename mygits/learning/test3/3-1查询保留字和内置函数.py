import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(dir(__builtins__))
print(len(dir(__builtins__)))
print("print is keyword:", "print" in keyword.kwlist)
print("or" in keyword.kwlist)
print("if is keyword:", "if" in keyword.kwlist,sep='')