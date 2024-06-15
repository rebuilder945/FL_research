lst=list(eval(input()))
Sum=sum(lst)
a=Sum/len(lst)
if Sum%len(lst)==0:
    print(int(a))
elif Sum%len(lst)!=0:
    print("%.2f"%(a))

