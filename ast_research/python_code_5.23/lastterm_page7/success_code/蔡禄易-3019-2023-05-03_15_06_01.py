a = input().split()
english = int(a[1])
python = int(a[2])
math = int(a[3])
total = int(a[1])+int(a[2])+int(a[3])
avg = total/3
del a[0]
b = a
b.sort(reverse=True)
f = int(b[0])
g = int(b[1])
h = int(b[2])
print(a[0],"%.2f"%f,"%.2f"%g,"%.2f"%h,"%.2f"%avg)

