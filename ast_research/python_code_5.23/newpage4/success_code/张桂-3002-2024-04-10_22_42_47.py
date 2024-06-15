ls = eval(input())
a = 0
b = 0
for i in ls:
    a = a+i
    b = b+1
e = a/b
if e - int(e) == 0: 
    print(int(e))
else:
    print("%.2f"%(e))
