m=input()
if m[0] in ['$','USD']:
    c=eval(m[1:-1])*6.78
elif m[0] in ['&','RMB']:
    c=eval(m[1:-1])/6.78
print("%.2f"%m)
