numbers=eval(input())
a,b=eval(input())
c=len(numbers)
if -c <= a< c and -c <= b < c:
    if a==b: print(numbers) 
    else: 
        del numbers[a:b] 
        print(numbers) 
    
else : print("error")


