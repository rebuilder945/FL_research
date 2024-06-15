money_str = input()
if money_str[0] == '&':
  rmb = eval(money_str[1:])
  usd = rmb / 6.78
  print("$%.2f" % usd)
elif money_str[0] == 'R' and money_str[1] == 'M' and money_str[2] == 'B':
  rmb = eval(money_str[3:])
  usd = rmb / 6.78
  print("USD%.2f" % usd)
elif money_str[0] == '$':
  usd = eval(money_str[1:])
  rmb = usd * 6.78
  print("&%.2f" % rmb)
elif money_str[0] == 'U' and money_str[1] == 'S' and money_str[2] == 'D':
  usd = eval(money_str[3:])
  rmb = usd * 6.78
  print("RMB%.2f" % rmb)
else:
  print("Error")
