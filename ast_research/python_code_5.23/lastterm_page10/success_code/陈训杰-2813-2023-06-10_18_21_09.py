s=input().split(" ")
s1=input()
s2=[]
for i in s:
    if s1 in i:
        i=i.repalce(s1,"")
    s2.append(i)
print(" ".join(s2))
