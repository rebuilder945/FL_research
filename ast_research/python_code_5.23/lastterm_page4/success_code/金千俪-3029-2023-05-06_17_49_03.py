name=list(input().split(","))
number=eval(input())
key=[[name[i],number[i]] for i in range(len(name))]
print(key)

