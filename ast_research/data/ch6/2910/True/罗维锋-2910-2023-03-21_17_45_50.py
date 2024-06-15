h=eval(input())
N=eval(input())
s=h
for x in range(1,N):
    s+=h
    h=0.5*h
print("{:.2f}".format(s))
