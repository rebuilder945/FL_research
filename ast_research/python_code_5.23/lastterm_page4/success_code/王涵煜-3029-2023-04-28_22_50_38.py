na=input()
num=eval(input())
name=na.split(",")
da=[]
for i in range(len(num)):
    ans=[]
    ans.append(name[i])
    ans.append(num[i])
    da.append(ans)
print(da)

