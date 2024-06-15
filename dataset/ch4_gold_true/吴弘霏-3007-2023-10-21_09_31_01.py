list=eval(input())
n,m=eval(input())
if n>=len(list) or m>=len(list):
        print("error")
elif n<=m:
        del list[n:m:1]
        print(list)
     

