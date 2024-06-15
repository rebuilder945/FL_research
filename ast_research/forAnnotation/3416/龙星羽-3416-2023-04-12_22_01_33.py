S= input()
if S[0] in ['$']:
    US = eval(S[1:])*6.78
    print('&%.2f'%US)
elif S[0] in ['&']:
    CH = eval(S[1:])/6.78
    print('&%.2f'%CH)
elif S[0:3] in ['USD']:
    US = eval(S[3:])*6.78
    print('&%.2f'%US)
elif S[0:3] in ['RMB']:
    CH = eval(S[3:])/6.78
    print('&%.2f'%CH)
else:
    print("Error")




