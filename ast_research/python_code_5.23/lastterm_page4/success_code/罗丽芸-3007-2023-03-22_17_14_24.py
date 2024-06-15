numbers=eval(input()) 
a,b=eval(input()) 
c=len(numbers) 
if -c <= a< c and -c <= b < c: 
    if ab: numbers.reverse() 
    d=c-a-1 
    e=c-b-1 
    del numbers[d:e] 
    numbers.reverse() 
    print(numbers)
    if a==b:
      print(numbers) 
else : print("error")
