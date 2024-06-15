a=input()
b=[]
print(a)
for i in a:
    if  i.isalpha():
        if ord(i)<ord("Z")+1:

            i=chr(26-(ord(i)-ord("A"))+ord("A")-1)
            print(i,end="")
        else:
            i=chr(26-(ord(i)-ord("a"))+ord("a")-1)
            print(i,end="")

    
    else:
        print(i,end='')

       
        





            


