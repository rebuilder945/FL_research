Is=eval(input())
n,m=eval(input())
del Is[n:m]
print(Is)
if n>m or n>len(Is) or m>len(Is):
    print("error")
