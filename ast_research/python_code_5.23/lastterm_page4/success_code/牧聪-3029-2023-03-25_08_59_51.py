a=input()
names=list[a.split(',')]
results=eval(input())
match=[[names[i],results[i]]for i in range(len(names))]
print(match)

