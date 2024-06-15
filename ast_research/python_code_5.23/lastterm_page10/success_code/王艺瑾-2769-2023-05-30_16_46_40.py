a=input()
b=[]
print(a)
for i in a:
    if  i.isalpha():
        if ord(i)<ord("Z")+1:

            i=chr(26-(ord(i)-ord("A"))+ord("A"))
            print(i,end="")
        else:
            i=chr(26-(ord(i)-ord("a"))+ord("a"))
            print(i,end="")

    
    else:
        print(i,end='')

       
        





            


