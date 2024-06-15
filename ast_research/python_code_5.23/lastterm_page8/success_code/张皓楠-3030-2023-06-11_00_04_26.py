names=input().split(",") 
grade=eval(input()) 
d=zip(names,grade) 
e=list(d) 
f=[] 
for i in e: 
    f.append(list(i)) 
    f.sort(key=lambda x:x[1]) 
print(f)

