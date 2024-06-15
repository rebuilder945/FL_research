a = input().split()
english = int(a[1])
python = int(a[2])
math = int(a[3])
total = int(a[1])+int(a[2])+int(a[3])
avg = total/3
t = a[0]
del a[0]
b = a
b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])
b.sort(reverse=True)
f = b[0]
g = b[1]
h = b[2]
print(t,"%.2f"%f,"%.2f"%g,"%.2f"%h,"%.2f"%avg)

