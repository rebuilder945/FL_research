num=input().split(" ")
avg=(int(num[1])+int(num[2])+int(num[3]))/3
ls=[num[1],num[2],num[3]]
print(ls)
ls.sort(reverse=False)
print(num[0],"{:.2f} {:.2f} {:.2f} {:.2f}".format(float(ls[0]),float(ls[1]),float(ls[2]),float(avg)))
