list=eval(input())
n,m=eval(input()) 
if n<=len(list) and m<=len(list):
    list[n:m]=[]
    print(list)
else:
    print("error")



    


