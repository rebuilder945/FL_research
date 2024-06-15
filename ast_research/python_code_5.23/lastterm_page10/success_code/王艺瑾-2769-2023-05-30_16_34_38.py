a=input()
b=[]
print(a)
for i in a:
    if  i.isalpha():
        i=chr(26-(ord(i)-ord("a")))
        print(i,end="")
    
    else:
        print(i,end='')

       
        





            


