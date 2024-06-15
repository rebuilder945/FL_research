s=input().split()
a=[]
for i in s:
    a.append(i)
a.sort(reverse=True)
dic=dict((("name",s[0]),("english",s[1]),("python",s[2]),("math",s[3])))
w=(int(s[1])+int(s[2])+int(s[3]))/3
dic["avg"]='w'
b=[int(s[1]),int(s[2]),int(s[3])]
print(dic["name"],"%.2f"%b[0],"%.2f"%b[1],"%.2f"%b[2],"%.2f"%w)
