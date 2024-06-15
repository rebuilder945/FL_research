a=eval(input())
a.sort(reverse=True)
b=()
for i in range(len(a)):
    b+=str(a[i])
print(int(b))
