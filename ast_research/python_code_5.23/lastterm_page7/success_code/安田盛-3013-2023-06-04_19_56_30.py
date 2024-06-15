n=input().split()
dic={}
while n[0]!="ok":
    dic[n[0]]=int(n[1])
    n=input().split()
a=list(dic.keys())
a.sort()
print(a)
b=list(dic.values())
b.sort()
print(b)
if "India" in a:
    print("yes")
else:
    print("no")
print(sum(b))



