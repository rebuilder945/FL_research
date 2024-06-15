iMoney = input()
if iMoney[0] in ['&']:
      C = (eval(iMoney[1:]))/6.78
      print("$%.2f"%(C))
elif iMoney[0:3] in ['RMB']:
      D = (eval(iMoney[3:]))/6.78
      print("USD%.2f"%(D))
elif iMoney[0] in ['$']:
      F = 6.78*(eval(iMoney[1:]))
      print("&%.2f"%(F))
elif iMoney[0:3] in ["USD"]:
      G = 6.78*(eval(iMoney[3:]))
      print("RMB%.2f"%(G))
else:
      print("Error")
