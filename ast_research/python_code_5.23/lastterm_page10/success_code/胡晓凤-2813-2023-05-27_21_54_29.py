a=list(input().split(" "))
b=input()
ls3=[]
for i in a:
    if i !=b:
        ls3.append(i)
ls=" ".join(ls3)
print(ls)

