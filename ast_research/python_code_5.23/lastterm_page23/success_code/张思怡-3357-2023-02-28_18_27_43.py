def Paodao(v,a): 
    return v*v/(2*a)
Flyname=input()
a=eval(input())
v=eval(input())
length=Paodao(v,a)
Fu="The acceleration of"
Shi="is"
Er="the take-off speed is"
Zhe="and the shortest take-off runway length is"
Danwei="M / s,"

#The acceleration of B350 is 3.57 M / s, the take-off speed is 60.00 M / s, 
# and the shortest take-off runway length is 503.92 M. 
print(Fu,Flyname,"is %.2f"%(a),Danwei,Er,"%.2f"%(v),Danwei,Zhe,"%.2f M."%(length))

