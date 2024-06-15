color1= input()
color2= input()       
lst=['red','blue','yellow']
if color1 not in ['red','blue','yellow']:
    print('error')
else:
    n1=lst.index(color1)
    if color2 not in ['red','blue','yellow']:
        print('error')
    else:
        n2=lst.index(color2)
        if n1 == n2:
            print('error')
        else:
            
            if n1==0 and n2==1 or n1==1 and n2==0:
                print("purple")
            elif n1==1 and n2==2 or n1==2 and n2==0:
                print('orange')
            else:
                print('green')


        


