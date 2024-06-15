ls=eval(input())
n=len(ls)
for i in range(n-1):
    if ls[i] in ls[i+1::1]:
        ls[i]="op"
while "op" in ls:
    ls.remove("op")
print(ls)


