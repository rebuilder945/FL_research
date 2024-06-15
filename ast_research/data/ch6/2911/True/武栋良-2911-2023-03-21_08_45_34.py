a = input()
n = len(a)
a = int(a)
lst = []
for i in range(1,n+1):
    b = a%10
    c = str((b+5)%10)
    a = a//10
    lst.append(c)
    s = " "
for x in lst:
    s = s+x
print(s.lstrip())
