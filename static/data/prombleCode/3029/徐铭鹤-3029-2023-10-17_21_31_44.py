names=input("")
names=names.split(',')
scores=input()
an=[]
for names,scores in zip(names,scores):
    a=[names,scores]
    an.attend(a)
    
print(an)

