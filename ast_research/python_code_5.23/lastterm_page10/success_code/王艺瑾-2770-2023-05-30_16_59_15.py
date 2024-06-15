a=input().split()
b=input().split()
for i in a:
    if i in b:
        b.remove(i)
if a!=[] or b!=[]:
    print("False")
elif len(a)!=len(b):
    print("False")
else:
    print("True")


        

       
        





            


