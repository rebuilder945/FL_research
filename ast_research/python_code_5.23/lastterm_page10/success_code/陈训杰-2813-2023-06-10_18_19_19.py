s=input().split(" ")
s1=input()
s2=[]
for i in s:
    for j in i:
        if j==s1:
            i=i.replace(j,"")
    s2.append(i)
print(" ".join(s2))
