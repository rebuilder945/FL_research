tour = []  # 反弹总高度
height = []  # 每次反弹高度

hei = eval(input()) # 起始高度
time = eval(input())  # 次数

for i in range(2, time + 2):
    # 第二次开始，落地时得距离应该是反弹高度*2
    if i == 2:
        tour.append(hei)
    else:
        tour.append(hei * 2)
    hei /= 2
    height.append(hei)


print('%.2f'%(sum(tour)))
