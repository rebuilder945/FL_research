ls=input().split(",")
ls1=eval(input())
ls2=[[ls[i],ls1[i]] for i in range(len(ls))]
ls2.sort(key=lambda x:x[1])
print(ls2)
