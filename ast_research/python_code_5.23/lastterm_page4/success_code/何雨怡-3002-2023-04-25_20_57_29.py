lst=eval(input())
he=sum(lst)
shu=len(lst)
av=he/shu
if av-av//1==0:
    print(int(av))
else:
    print("%.2f"%(av))
