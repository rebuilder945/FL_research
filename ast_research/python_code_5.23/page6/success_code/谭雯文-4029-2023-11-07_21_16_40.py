a,b=map(int,input().split())
if 10>a>b or b-a<3 :
    print("illegal input")
elif a==0 and b==3:
    print("102 120 201 210")
else:
    a1=str(a)+str(a+1)+str(a+2)
    a2=str(a)+str(a+2)+str(a+1)
    a3=str(a+2)+str(a)+str(a+1)
    a4=str(a+2)+str(a+1)+str(a)
    a5=str(a+1)+str(a+2)+str(a)
    a6=str(a+1)+str(a)+str(a+2)
    print(int(a1),int(a2),int(a3),int(a4),int(a5),int(a6))






