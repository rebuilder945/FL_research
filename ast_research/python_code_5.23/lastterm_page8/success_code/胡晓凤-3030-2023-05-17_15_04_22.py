ls1=input().split(",")
ls2=input().split(",")
ls3=()
ls4=[]
for i in range(len(ls1)):
    ls3=(ls1[i],ls2[i])
    ls4.append(ls3)
    ls4.sort(key=lambda ls2:ls2[i])
print(ls4)
