huobi = input()
#人民币转换为美元
if huobi[0] == "&":
    renminbi = eval(huobi[1:])
    meiyuan = renminbi / 6.78
    print("$%.2f"%(meiyuan))
elif huobi[0:3] == "RMB":
    renminbi = eval(huobi[3:])
    meiyuan = renminbi / 6.78
    print("USD%.2f"%(meiyuan))
#美元转换为人民币
elif huobi[0] == "$":
    meiyuan = eval(huobi[1:])
    renminbi = meiyuan * 6.78
    print("&%.2f"%(renminbi)) 
elif huobi[0:3] == "USD":
    meiyuan = eval(huobi[3:])
    renminbi = meiyuan * 6.78
    print("RMB%.2f"%(renminbi))
else:
    print("Error")
