list=eval(input())
n,m=eval(input())
if n in len(list):
    del list[n:m]
    print(list)
else:
    print("error")
