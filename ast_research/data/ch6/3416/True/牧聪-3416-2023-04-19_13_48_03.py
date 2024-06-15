money=input()
if money[0] in ['&']:
    c=(eval(money[1:])/6.78)
    print("$"'%.2f'%c)
elif money[0:3] in ['RMB']:
    c=(eval(money[3:])/6.78)
    print("USD"'%.2f'%c)
elif money[0:3] in ['USD']:
    c=(eval(money[3:])*6.78)
    print("RMB"'%.2f'%c)
elif money[0] in ['$']:
    c=(eval(money[1:])*6.78)
    print("&"'%.2f'%c)
else:
    print("Error")

