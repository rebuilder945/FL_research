shulie = eval(input())
xinshulie = shulie.copy()
for x in shulie:
    cishu = shulie.count(x)
    if cishu == 1:
        pass
    else: 
        if xinshulie.count(x) != 1:
            for i in range(0,cishu-1):
              xinshulie.remove(x) 
        else:
            pass
print(xinshulie)  
