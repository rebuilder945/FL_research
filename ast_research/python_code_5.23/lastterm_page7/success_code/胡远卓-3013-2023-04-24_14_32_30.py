dic={}
str=input()
while str!="ok":
    name,val=str.split()
    val=eval(val)
    dic[name]=val
    str=input()
print(sorted(list(dic.keys())))
print(sorted(list(dic.values())))
print("yes" if "India" in dic else "no")
print(sum(dic.values()))
