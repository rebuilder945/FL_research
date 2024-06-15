h=eval(input())
N=eval(input())
H=h
for i in range(N-1):
    h1=h*(0.5)**(i+1)
    H+=h1*2
print("%.2f" %H)
