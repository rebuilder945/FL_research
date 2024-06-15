a = input()
h = ['USD','RMB']
lei = ['$','&']
if a[0] ==lei[0] :
    b = eval(str(a[1:]))*6.78
    print("&%.2f"%(b))
elif a[0]==lei[1]:
    c = eval(str(a[1:]))/6.78
    print("$%.2f"%(c))
elif a[:3]==h[1]:
    d = eval((str(a[3:]))/6.78
    print("USD%.2f"%(d))
elif a[:3]==h[0]:
    e = eval(str(a[3:]))*6.78
    print("RMB%.2f"%(e))
else:
    print("Error")
