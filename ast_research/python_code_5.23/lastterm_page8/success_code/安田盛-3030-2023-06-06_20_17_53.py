s=input().split(",")
n=list(map(int,input().split(",")))
x=[[s[i],n[i]]for i in range(len(s))]
x.sort(key=lambda x:x[1])
print(x)




            




