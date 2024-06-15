lt=eval(input())
a,b=eval(input())
l=len(lt)
if a>l-1 or b>l-1 or -a<-l or a>b:
    print("error")
else:
    lt[a:b]=[]
    print(lt)
