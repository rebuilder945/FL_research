Mo=input()
if Mo[0] in ['$']: 
    Ren=eval(Mo[1:])*6.78
    print("&%.2f"%(Ren))
elif Mo[0] in ['U','u']:
    Ren=eval(Mo[3:])*6.78 
    print("RMB%.2f"%(Ren))
elif Mo[0] in ['&']:   
    Mei=eval(Mo[1:])/6.78
    print("$%.2f"%(Mei))
elif Mo[0] in ['R','r']:
    Mei=eval(Mo[3:])/6.78
    print("USD%.2f"%(Mei))
else:
    print('Error')
