v = int(input())
l = int(input())
r = (v-l)/l
if v<=l:
    print("未超速")
elif r<=0.1:
    print("超速警告")
elif r>0.1 and r<=0.2:
    print("罚款100元")
elif r>0.2 and r<=0.5:
    print("罚款500元")
elif r>0.5 and r<=1:
    print("罚款1000元")
elif r>1:
    print("罚款2000元")
