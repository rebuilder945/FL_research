ls1=input().split(",")
ls2=eval(input())
ls3=[[ls1[i],ls2[i]] for i in range(1,len(ls1)-1)]
print(ls3)
