s=input().split()
a=[]
for i in s:
    a.append(i)
a.sort(reverse=True)
dic=dict((("name",a[0]),("english",a[1]),("python",a[2]),("math",a[3])))
w=(int(a[1])+int(a[2])+int(a[3]))/3
dic["avg"]='w'
b=[int(a[1]),int(a[2]),int(a[3])]
print(dic["name"],"%.2f"%b[0],"%.2f"%b[1],"%.2f"%b[2],"%.2f"%w)
