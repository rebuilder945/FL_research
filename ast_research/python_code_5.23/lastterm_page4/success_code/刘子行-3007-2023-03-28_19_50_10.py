shit=eval(input())
n,m=eval(input())
if n>len(shit)-1 or m>len(shit)-1 :
    print("error")
else:
    if n<=m:
        del shit[n:m]
    else:
        del shit[n:m:-1]
    print(shit)
