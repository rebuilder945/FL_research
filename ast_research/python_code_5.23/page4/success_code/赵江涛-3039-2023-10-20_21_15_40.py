from ipaddress import ip_address


ls = eval(input())
ls2 = list(set(ls))
ls2.pop(0)
ls2.pop(-1)
print(ls2)
