s=input().split(" ")
s1=input()
s2=[]
for i in s:
    for j in i:
        if j==s1:
            i=i.replace(j,"")
    if i!="":
        s2.append(i)
print(s2)
print(" ".join(s2))
