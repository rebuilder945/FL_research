A = eval(input())
X = 0
for i in A:
    X += i
M = X/(int(len(A)))
if M - int(M) == 0:
    print(int(M))
else:
    print("%.2f"%(M))
    
