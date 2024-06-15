a=eval(input())      
if 0<a<11 or 18<a<29:
    if a%2==0:
        print("black")
    else:
        print("red")    
elif 10<a<19 or 28<a<37:
    if a%2==0:
        print("red")
    else:
        print("black") 
elif a==0:
    print("grren")      
else:
    print("error")
