
a=eval(input())
def s(a):
    b,c,d=int
    a=b*100+c*10+d
    if a==b**3+c**3+d**3:
        return True
    else:
        return False
e=[]
for i in range(100,a):
    if s(i):
        print(i)
        e.append(i)
if e==[]:
    print("none")
    

