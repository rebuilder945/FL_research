lst=eval(input())
b=0
for i in range(len(lst)):
    b+=lst[i]
a=b/len(lst)
print("%.2f"%(a))
