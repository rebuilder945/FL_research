def ave(score_list):
    a1 = min(score_list)
    a2 = score_list.index(a1)
    del score_list[a2]
    b=[x for x in score_list if x<max(score_list)]
    c=sum(b)/3
    d=round(c,2)
    return d



