name=input()
grade=eval(input())
new=[]
for i in len(name):
    new=[x+y for x in name[i] for y in grade[i]]
print(new)
    
