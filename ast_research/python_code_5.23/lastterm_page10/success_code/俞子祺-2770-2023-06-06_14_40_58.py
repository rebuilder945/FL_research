n=input()
m=input()
ls=[]
for x in n:
    if len(m)==len(n):
        if x in m:
            ls.append(x)
if len(ls)==len(n):
    print("True")
else:
    print("False")
