s=input().split()
dic={}
while s!="ok":
    dic[s[0]]=int(s[1])
    s=input()
a=list(dic.values())
a.sort()
print(list(dic.keys()))
print(a)
if "India"in dic:
    print("yes")
else:
    print("no")
print(sum(a))



            




