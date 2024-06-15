n=input()
a=0
for x in range(100,int(n)):
    if x==eval(n[0])**3+eval(n[1])**3+eval(n[2])**3:
        print(int(x))
        a+=1
if a==0:
    print('none')        
