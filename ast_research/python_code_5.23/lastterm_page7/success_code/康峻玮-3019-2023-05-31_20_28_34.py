m=input().split(" ")
stu=dict((("name",m[0]),("english",m[1]),("python",m[2]),("math",m[3])))
a=(int(m[1])+int(m[2])+int(m[3]))/3
ls=[int(m[1]),int(m[2]),int(m[3])]
ls.sort(reverse=True)
print(m[0],"%.2f %.2f %.2f %.2f" % (float(m[1]),float(m[2]),float(m[3]),a))

