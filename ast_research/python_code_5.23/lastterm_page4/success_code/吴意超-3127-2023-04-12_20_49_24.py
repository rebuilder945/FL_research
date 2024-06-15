a = eval(input())
b = [i for i in range(1,a+1)]
c= b[0]
for i in range(0,len(b)-1):
    b[i] =b[i+1]
b[-1] = c
print(b)
