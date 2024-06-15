shit=eval(input())
for x in shit:
    for i in range(2,x):
        if x%i==0:
            shit.remove(x)
print(shit)
