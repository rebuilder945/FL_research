a = eval(input())
flag = True
for i in range(a+1):
    A = i // 100
    B = i // 10 % 10
    C = i % 10
    if A**3+B**3+C**3 == a:
        print(i)
        flag=False
if flag==True:
    print("none")
        
    





