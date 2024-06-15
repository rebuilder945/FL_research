Coinstr = input()
if Coinstr[0:3] in ['RMB']:
        USD = (eval(Coinstr[3:]))/6.78
        print('USD%.2f'% USD)
elif Coinstr[0] in ['&']:
        USD = (eval(Coinstr[1:]))/6.78
        print('$%.2f'% USD)
elif Coinstr[0:3] in ['USD']:
        RMB = (eval(Coinstr[3:]))*6.78
        print('RMB%.2f'% RMB)
elif Coinstr[0] in ['$']:
        RMB = (eval(Coinstr[1:]))*6.78
        print('&%.2f'% RMB)
else:
    print("Error")
