a=input()
s1="abcdefghijklmnopqrstuvwxyz"
s2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ls1=(x for x in s1)
ls2=(x for x in s2)
for i in range(26):
    if a[i] in s1 or a[i] in s2:
        print(a[26-i],end="")
    else:
        print(a[i],end="")
