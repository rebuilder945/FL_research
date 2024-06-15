# 美元人民币转换
# 人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：
# 人民币和美元间汇率固定为：1美元 = 6.78人民币。
# 程序可以接受人民币或美元输入，转换为美元或人民币输出。
# 人民币采用&符号或RMB表示，美元采用$或USD表示，符号和数值之间没有空格。
# 注意：人民币和美元间符号在转换中要对等，&和$相互对应，RMB和USD相互对应。

CurrencyStr = input()
if CurrencyStr[0] in ['&']:
    USD = eval(CurrencyStr[1:]) / 6.78
    print("$%.2f"%(USD))
elif CurrencyStr[0] in ['$']:
    RMB = eval(CurrencyStr[1:]) * 6.78
    print("&%.2f"%(RMB))
elif CurrencyStr[0:3] in ['RMB', 'rmb']:
    USD = eval(CurrencyStr[3:]) / 6.78
    print("USD%.2f"%(USD))
elif CurrencyStr[0:3] in ['USD', 'usd']:
    RMB = eval(CurrencyStr[3:]) * 6.78
    print("RMB%.2f"%(RMB))
else:
    print("Error")
