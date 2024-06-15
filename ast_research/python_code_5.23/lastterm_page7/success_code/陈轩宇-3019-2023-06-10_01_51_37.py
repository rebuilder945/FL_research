a = input().split(" ")
b = a[0]
del a[0]
a = list(map(int,a))
a.sort(reverse=True)
avg = sum(a)/len(a)
a.append(avg)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(b,a[0],a[1],a[2],a[3]))

