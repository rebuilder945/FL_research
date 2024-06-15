#人民币和美元间汇率固定为：1美元 = 6.78人民币。
#程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用&符号或RMB表示，美元采用$或USD表示，符号和数值之间没有空格。
#注意：人民币和美元间符号在转换中要对等，&和$相互对应，RMB和USD相互对应。
money = input()
if money[0] == "&":
    dollar = float(money[1::])/6.78
    print("{}{:.2f}".format("$",dollar))
elif money[:3:] == "RMB":
    dollar = float(money[3::])/6.78
    print("{}{:.2f}".format("USD",dollar))
elif money[0] == "$":
    yuan = float(money[1::])*6.78
    print("{}{:.2f}".format("&",yuan))
else:
    yuan = float(money[3::])*6.78
    print("{}{:.2f}".format("RMB",yuan))
