lst=eval(input())
b=0
for i in range(len(lst)):
    b+=lst[i]
a=b/len(lst)
if a%1==0:
    print(a)
else:
    print("%.2f")%(a)
