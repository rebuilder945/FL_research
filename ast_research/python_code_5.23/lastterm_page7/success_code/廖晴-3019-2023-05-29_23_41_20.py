s=input().split( )
name=s[0]
del s[0]
for i in range(len(s)):
    s[i]=int(s[i])
s.sort(reverse=True)
avg=(s[0]+s[1]+s[2])/3
print(name,"%.2f %.2f %.2f %.2f" %(s[0],s[1],s[2],avg))
