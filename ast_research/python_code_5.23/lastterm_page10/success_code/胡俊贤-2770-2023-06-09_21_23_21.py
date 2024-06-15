a=input()
b=input()
A={}
B={}
for i in a:
    A[i]=a.count(i)
for i in b:
    B[i]=b.count(i)
if A==B:
    print("True")
else:
    print('False')
    


