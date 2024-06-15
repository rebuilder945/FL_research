import numpy as np
a=eval(input())
avr=np.sum(a)/len(a)
avri=int(avr)
if avr>avri:
    print("%.2f"%avr)
else:
    print(avri)

