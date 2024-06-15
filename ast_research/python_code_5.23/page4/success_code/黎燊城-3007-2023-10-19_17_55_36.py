list=eval(input())
a,b=eval(input())
if  (a or b) >(len(list)-1):
    print("error")
else :
     del list[a:b]
     print(list)

