n = eval(input())
for i in range(100,int(n)):
    a = int(i%10)
    i = i//10
    b = int(i%10)
    i = i//10
    c = int(i%10)
    if a**3+b**3+c**3 ==i:
        print(i)
else:
    print("None")
    
    

