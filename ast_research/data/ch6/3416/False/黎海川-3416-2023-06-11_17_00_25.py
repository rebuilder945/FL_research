m = input()
if m[-1] in ['RMB', '&']:
    USD = eval(m[0: -1]) / 6.78
    print("%.2fUSD" % (USD))
elif m[-1] in ['USD', '$']:
    RMB = 6.78 * eval(m[0:-1])
    print("%.2f" % (RMB))
else:
    print('Error')


