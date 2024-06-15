a=input()
b=0
for i in list(a):
    if i in list("123456789"):
        b+=1
        break
for i in list(a):
    if i in list("zxcvbnmlkjhgfdsaopiuytrewq"):
        b+=1
        break
for i in list(a):    
    if i in list("ZXCVBNMLKJHGFDSAPOIUYTREWQ"):
        b+=1
        break
for i in list(a):
    if len(a)>=8:
        b+=1
for i in list(a):    
    if i in list("~!@#$%^&*()<>:][}{/?-_=+"):
        b+=1
        break
print(b)
