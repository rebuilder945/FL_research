i=eval(input())
n,m=eval(input())
if n>len(i)-1 or m>len(i)-1:
    print("error")
else:
    if n>m:
       del i[n:m:-1]
    else:
        del i[n:m]
print(i)
