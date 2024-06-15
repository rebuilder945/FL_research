T = input()
if T[0] in ['&']:
   C = (eval(T[1:]) /6.78)
   print('$%.2f'%(C))
elif T[0] in ['$']:
   D = (eval(T[1:])*6.78)
   print('&%.2f'%(D))
elif T[0:3] in ['RMB','rmb']:
   F = (eval(T[3:]) /6.78)
   print('USD%.2f'%(F))
elif T[0:3] in ['usd','USD']:
   G= (eval(T[3:])*6.78)
   print('RMB%.2f'%(G))
else:
   print('Error')

