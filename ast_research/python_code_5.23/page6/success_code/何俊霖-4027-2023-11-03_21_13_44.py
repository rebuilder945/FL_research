x=input()
sum=0
while x!='#':
    sum+=int(x)
    x=int(input())
if x == '#':
    print(sum)
