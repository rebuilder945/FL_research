

a=input().split(' ')
a.sort(reverse=True)
ave=(int(a[1])+int(a[2])+int(a[3]))/3
a.append(ave)
print(a[0],a[1],a[2],a[3])
