n=eval(input())
numbers=[x for x in range(n+1)]
s=[i for i in numbers[1:n+1]]

for y in numbers[0:n-1]:
    s[y]=y+2
    
s[n-1]=1

print(s)
