name=list(input().split(","))
result=eval(input())
values = [[name[i],result[i]] for i in range(len(name))]
print(values)
