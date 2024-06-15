smoney=input()
if smoney[0] in ['$']:
    C=(eval(smoney[1:])) *6.78  
    print('&%.2f'%C) 
elif smoney[0] in ['R']:
    D=(eval(smoney[3:]))/6.78
    print('USD%.2f'%D)
elif smoney[0] in ['U']:
    C=(eval(smoney[3:]))*6.78
    print('RMB%.2f'%C)
elif smoney[0] in ['&']:
    D=(eval(smoney[1:]))/6.78
    print('$%.2f'%D)
else:
      print("Error")

