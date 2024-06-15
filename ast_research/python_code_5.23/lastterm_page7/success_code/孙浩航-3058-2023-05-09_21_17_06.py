names={}
s=input()
while s!="q":
    names[s]=names.get(s,0)+1
    s=input()

print(max(names,key=names.get),end=" ")      #将返回一个字典x的值最大的项。即对应于最大值的键。
print(max(names.values()))
