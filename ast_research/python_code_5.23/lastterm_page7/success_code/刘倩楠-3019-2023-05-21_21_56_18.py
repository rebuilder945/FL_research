m=input().split(" ")
stu=dict((("name",m[0]),("english",m[1]),("python",m[2]),("math",m[3])))
avg=(int(m[1])+int(m[2])+int(m[3]))/3
num=[m[1],m[2],m[3]]
num.sort(reverse=True)
print(m[0],"{:.2f} {:.2f} {:.2f} {:.2f}".format(float(num[0]),float(num[1]),float(num[2]),float(avg)))
