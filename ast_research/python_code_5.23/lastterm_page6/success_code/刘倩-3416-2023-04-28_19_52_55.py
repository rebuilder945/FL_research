shuru = input()
if shuru[0] == '$':
    shuchu = (eval(shuru[1:])*6.78)
    print("&%.2f"%(shuchu))

elif shuru[0] == '&':
    shuchu = eval(shuru[1:])/6.78
    print("$%.2f"%(shuchu))

elif shuru[0:3] == 'RMB':
    shuchu = eval(shuru[3:])/6.78
    print("USD%.2f"%(shuru))

elif shuru[0:3] == 'USD':
    shuchu = eval(shuru[3:])*6.78
    print("RMB%.2f"%(shuchu))

else:
    print('Error')
