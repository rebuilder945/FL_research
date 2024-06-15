Name=input()
a=eval(input())
v=eval(input())
length=v*v/(2*a)
x1="The acceleration of"
x2="M / s, the take-off speed is"
x3="M / s, and the shortest take-off runway length is"
print(x1,Name,"is",'%.2f'%(a),x2,'%.2f'%(v),x3,'%.2f'%(length),"M.")
