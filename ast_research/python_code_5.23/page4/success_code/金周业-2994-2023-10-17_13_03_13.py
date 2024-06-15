string=list(eval(input()))
n,m=eval(input())
x=string[n]
if n < len(string):
    for i in range(m):
        string.append(x)
else:
    string="error"
print(string)


