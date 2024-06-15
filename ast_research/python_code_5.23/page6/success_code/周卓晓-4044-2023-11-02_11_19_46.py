a = eval(input())
flag = True
for i in range(100,a+1):
    A = i // 100
    B = i // 10 % 10
    C = i % 10
    if A**3+B**3+C**3 == i:
        flag=False
        print(i)
if flag==True:
    print("none")
        
    





