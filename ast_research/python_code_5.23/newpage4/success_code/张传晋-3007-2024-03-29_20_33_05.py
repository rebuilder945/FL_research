lst = eval(input())
n,m = eval(input())
lstCopy1 = lst[:n]
lstCopy2 = lst[m:]
cum = []
lst_num = len(lst)
if n>lst_num or m>lst_num:
    print("error")
else:
    lstCopy1.extend(lstCopy2)
    print(lstCopy1)
    # while len(lst)>0:
    #     if lst[lst_num-1] not in lstCopy:
    #         cum.append(lst[lst_num-1])
    #     lst_num-=1
    # cum.reverse()
    # print(cum)

