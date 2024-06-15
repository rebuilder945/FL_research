a,b=input().split()
if int(b)-int(a)==3:
    for i in range(int(a)*100,int(b)*100):
        if i//100!=i//10%10!=i%10 and int(a)<=i//100<=int(b) and int(a)<=i//10%10<=int(b) and int(a)<=i%10<=int(b):
            print(i,end=' ')
else:
    print("illegal input")
