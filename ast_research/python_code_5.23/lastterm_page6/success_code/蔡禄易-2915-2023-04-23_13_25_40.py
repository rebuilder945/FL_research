ha = eval(input())
shui = 0
for i in range(101,ha):
    a=eval(str(i)[0]) 
    b=eval(str(i)[1])  
    c=eval(str(i)[2])    
    if i == a*a + b*b + c*c:
        shui += 1
        print(i)
if shui == 0:
    print("none")
