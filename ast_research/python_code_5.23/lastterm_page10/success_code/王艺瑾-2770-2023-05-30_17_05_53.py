a=input()
b=input()
c=[x for x in a]
d=[i for i in b]
for i in c:
    if i in d:
        d.remove(i)
if c!=[] or d!=[]:
    print("False")
elif len(c)!=len(d):
    print("False")
else:
    print("True")

        

       
        





            


