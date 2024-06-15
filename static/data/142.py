money = input()

if money[0] == "$":
    rmb = eval(money[1:]) * 6.78
    print("&{:.2f}".format(rmb))
elif money[0] == "&":
    usd = eval(money[1:]) / 6.78
    print("RMB{:.2f}".format(usd))
elif money[:3] == "RMB":
    rmb = eval(money[3:]) / 6.78
    print("${:.2f}".format(rmb))
elif money[:3] == "USD":
    usd = eval(money[3:]) * 6.78
    print("RMB{:.2f}".format(usd))
else:
    print("Error")
#使用print("&{:.2f".format(rmb))和print("RMB{:.2f}".format(usd))时漏掉了闭合的括号 )，导致了 "unmatched '{' in format spec" 错误。