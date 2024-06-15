numbers=list(eval(input()))
a,b=map(int,input().split(","))
c=len(numbers)
del numbers[a:b]
if a<c and b<c:
    print(numbers)
else:
    print("error")
    
