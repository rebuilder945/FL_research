names=list(input().split(","))
grades=eval(input())
cnames=names.pop(names[0])
mnames=cnames.insert(2,names[0])
t=[[mnames[i],grades[i]] for i in range(len(grades))]
print(t)

