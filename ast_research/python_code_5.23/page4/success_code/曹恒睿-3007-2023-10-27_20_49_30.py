shulie=eval(input())
qidian,zhongdian=eval(input())
zongshuliang=len(shulie)
xinliebiao=[]
if zhongdian  > zongshuliang or qidian >zongshuliang:
    print("error")
else:   
    shanchudefanwei=list(range(qidian,zhongdian))
    for x in shulie:
        if shulie.index(x) not in shanchudefanwei:
            xinliebiao.append(x)
        else:
            pass
    print(xinliebiao)
   

