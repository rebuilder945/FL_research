a=list(input())
b=input()
for i in a:
    if i==b:
       a[a.index(i)]="#"
print("".join(a))
