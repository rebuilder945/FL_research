string=list(eval(input()))
n,m=eval(input())
if n < len(string):
    for i in range(m):
        x=string[n]
        string.append(x)
else:
    string="error"
print(string)


