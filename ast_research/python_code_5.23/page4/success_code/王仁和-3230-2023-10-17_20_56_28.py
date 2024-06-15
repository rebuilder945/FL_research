a,b,c,d=eval(input())
grade=a+b+c+(d*0.7)
lg=(60-a-b-c)/0.7
if d>= 40:
    print("%.2f" % (grade))
else:
    print("%.2f"%(d))
print("%.2f"%(lg))

