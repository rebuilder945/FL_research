a=input()
l1="1234567890"
l2="\~!@#$%^&*()_=-/,.?<>;:[]{}|"
c=0
for i in a:
    if i in l1:
        c+=1
        break
for i in a:
    if i in l2:
        c+=1
        break
if len(a)>=8:
    c+=1
for i in a:
    if i.islower():
        c+=1
        break
for i in a:
    if i.isupper():
        c+=1
        break
print(c)


    



        

       



                    




