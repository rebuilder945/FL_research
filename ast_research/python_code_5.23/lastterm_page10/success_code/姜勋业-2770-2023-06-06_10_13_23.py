a=list(input())
b=list(input())
k=[]
for i in range(len(a)):
    if a[i] in b:
        k.append(a[i])
if len(k)<len(a):
    print(False)
else:
    print(True)
