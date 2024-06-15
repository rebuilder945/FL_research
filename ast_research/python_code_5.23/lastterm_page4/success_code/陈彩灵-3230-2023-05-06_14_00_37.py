ls1 = eval(input())
ls1.sort(reverse=True)
x =''
for i in range(len(ls1)):
    x+=str(ls1[i])  
if x.startswith('0'): 
    print(0)
else:
    print(x)

