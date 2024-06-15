numbers=eval(input())
x=0
for i in range(0,len(numbers)):
    a=max(numbers)
    x+=a*(10**(len(numbers)-1))
    numbers.remove(a)
print(x)
