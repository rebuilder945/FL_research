Q=input()
if Q[0] in ['U']:
    a = eval(Q[3:])*6.78
    print("RMB""%.2F"%(a))
elif Q[0] in ['R']:
    b = eval(Q[3:]) /6.78
    print("USD""%.2f"%(b))
elif Q[0] in ['&']:
    c = eval(Q[1:]) /6.78
    print("$""%.2f"%(c))
elif Q[0] in ['$']:
    d = eval(Q[1:]) *6.78
    print("&""%.2f"%(d))

else:
    print("Error")

