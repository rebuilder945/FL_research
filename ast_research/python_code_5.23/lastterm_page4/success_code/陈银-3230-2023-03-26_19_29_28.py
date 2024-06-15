a = eval(input())
a.sort(reverse = True)
c = ''
for x in range(0,len(a)):
        c+=str(a[x])
print(int(c))
