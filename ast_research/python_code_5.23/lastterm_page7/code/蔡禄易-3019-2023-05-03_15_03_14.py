a = input().split()
english = int(a[1])
python = int(a[2])
math = int(a[3])
total = int(a[1])+int(a[2])+int(a[3])
avg = total/3
b = del(a[0])
b.sort(reverse=True)
print(a[0],"%.2f"%b[0],"%.2f"%b[1],"%.2f"%b[2],"%.2f"%avg)

