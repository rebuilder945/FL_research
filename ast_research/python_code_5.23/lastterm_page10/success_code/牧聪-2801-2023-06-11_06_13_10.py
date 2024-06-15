a=[x for x in input()]
point=0
thing="\\~!@#$%^&*()_=-/,.?<>;:[]}{|"
if len(a)>8:
    point+=1
for i in a:
    if i.isdigit():
        point+=1
        break
for i in a:    
    if i.islower():
        point+=1
        break
for i in a:
    if i.isupper():
        point+=1
        break
for i in a:
    if i in thing:
        point+=1
        break
print(point)



