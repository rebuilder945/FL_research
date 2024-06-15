n = input()
if n[0]=='$':
    print("&%.2f"%(eval(n[1:])*6.78))
elif n[0]=='&':
    print("$%.2f"%(eval(n[1:])/6.78))
elif n[:3] in ['RMB']:
    u = eval(n[3:]) / 6.78
    print("USD{:.2f}".format(u))
elif n[:3] in ['USD']:
    r = 6.78 * eval(n[3:])
    print("RMB{:.2f}".format(r))
else:
    print("Error")

