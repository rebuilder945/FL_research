a = input()
if a[0] in ['&']:
    USD = eval(a[1:])/6.78
    print('$%.2f' %USD)
elif a[0] in ['R']:
    USD = eval(a[3:])/6.78
    print('USD%.2f' %USD)
elif a[0] in ['$']:
    RMB =eval(a[1:])*6.78
    print('&%.2f' %RMB)
elif a[0] in ['U']:
    RMB =eval(a[3:])*6.78
    print('RMB%.2f' %RMB)
else:
    print('Error')



