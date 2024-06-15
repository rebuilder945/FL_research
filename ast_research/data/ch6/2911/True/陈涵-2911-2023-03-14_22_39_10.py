a=input("")
s=[(int(a[i])+5)% 10 for i in range(len(a))]
s2=[str(s[i]) for i in range(len(s))]
s2.reverse()
print("".join(s2)) 

