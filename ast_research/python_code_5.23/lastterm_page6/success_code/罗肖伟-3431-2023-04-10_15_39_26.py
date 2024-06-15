x=eval(input())
if x==0:
    print("green")
elif x in range(1,11) or x in range(19,29):
    if x%2==0:
        print("black")
    else:
        print("red")  
elif x in range(11,19) or x in range(29,37) :
    if x%2==0:
        print("red")
    else:
        print("black")
else:
    print("error")        
              
