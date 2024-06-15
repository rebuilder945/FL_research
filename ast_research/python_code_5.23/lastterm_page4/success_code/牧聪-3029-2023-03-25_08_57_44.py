names=input()
names_list=names.split(',')
results=eval(input())
match=[[names[i],results[i]]for i in range(len(names))]
print(match)

