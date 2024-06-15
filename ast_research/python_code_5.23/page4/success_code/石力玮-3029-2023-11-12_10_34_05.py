name=list(eval(input()))
grade=eval(input())
new=[]
for name,grade in zip(name,grade):
    new.append([name,grade])
print(new)

