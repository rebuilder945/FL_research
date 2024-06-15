lst=eval(input())
b=0
for i in range(len(lst)):
    b+=lst[i]
a=b/len(lst)
if type(a)==int():
    print(a)
elif type(a)==float():
    print("%.2f")%(a)
