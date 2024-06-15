a=input()
b=[]
for i in a:
    if  i.isalpha():
        i=chr(26+ord(i)-1)
        print(i,end="")
    
    else:
        print(i,end='')
print(a)
       
        





            


