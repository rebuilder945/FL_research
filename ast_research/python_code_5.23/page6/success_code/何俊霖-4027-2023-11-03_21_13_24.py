x=input()
sum=0
while x!='#':
    sum+=int(x)
    x=int(input(x))
if x == '#':
    print(sum)
