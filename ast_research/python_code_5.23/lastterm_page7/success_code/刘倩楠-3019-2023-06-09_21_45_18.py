n=input().split(" ")
a=list(map(int,n[1:]))
a.sort()
avg=(int(n[1])+int(n[2])+int(n[3]))/3
print(n[0],"{:.2f} {:.2f} {:.2f} {:.2f}".format(float(a[0]),float(a[1]),float(a[2]),avg))
