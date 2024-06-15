a=eval(input())
if (a>=1 and a<=10) or (a>=19 and a<=28):    
    if a%2==0:        print('black')    
    else:        
        print('red')
elif (a>=11 and a<=18) or (a>=29 and a<=36):    
    if a%2==0:        
        print("red")    
    else:        
        print('black')
elif a==0:    
    print('green')
else :    
    print("error")

