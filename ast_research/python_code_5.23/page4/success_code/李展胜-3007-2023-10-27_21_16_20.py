a=[eval(input())]
list=list(a)
n,m=eval(input())
if n>len(list)-1 or m>len(list)-1:
    print("error")
else:
    del list[n:m] 
    print(list)   

