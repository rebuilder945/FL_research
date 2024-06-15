Is=eval(input())
n,m=eval(input())
if n>m or n>len(Is) or m>len(Is):
    print("error")
else:
    del Is[n:m]
    print(Is)
