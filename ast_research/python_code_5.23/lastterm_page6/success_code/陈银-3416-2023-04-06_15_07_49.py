a = input()
h = ['USD','RMB']
if a[0] == ['$']:
    b = int(str(a[1:]))*6.78
    print("&%.2f"%(b))
elif a[0]==['&']:
    c = int(str(a[1:]))/6.78
    print("$%.2f"%(c))
elif a[:3]==h[1]:
    d = int(str(a[3:]))/6.78
    print("USD%.2f"%(d))
elif a[:3]==h[0]:
    e = int(str(a[3:]))*6.78
    print("RMB%.2f"%(e))
else:
    print("Error")
