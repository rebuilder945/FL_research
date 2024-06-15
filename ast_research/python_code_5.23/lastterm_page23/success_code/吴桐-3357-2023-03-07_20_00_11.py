def paodao(v,a):
    length=v*v/(2*a)
    return length
mincheng=input()
a=eval(input())
v=eval(input())
L=paodao(v,a)
shuchu="The acceleration of %s is %.2f M / s,the take-off speed is %.2f M / s,and the shortest take-off runway length is %.2f M."%(mincheng,a,v,L)
print(shuchu)
