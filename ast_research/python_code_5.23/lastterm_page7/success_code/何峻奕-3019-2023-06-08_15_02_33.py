s=input().split()
a=[]
for i in s:
    a.append(i)
a.sort(reverse=True)
dic={("name",s[0]),("english",s[1]),("python",s[2]),("math",s[3])}
dic["avg"]=round(sum(int(s[1])+int(s[2])+int(s[3]))/3,2)
b=[int(s[1]),int(s[2]),int(s[3])]
print(dic["name"],"%.2f"%b[0],"%.2f"%b[1],"%.2f"%b[2],dic["avg"])
