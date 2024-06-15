a = eval(input())
n,m = eval(input())
if(n>m or n<0 or n>len(a) or m<0 or m>len(a)):
    print("error")
else :
    for i in range(len(a)):
        if i in range(n+1,m+1):
        a.remove(i)
        print(a)
