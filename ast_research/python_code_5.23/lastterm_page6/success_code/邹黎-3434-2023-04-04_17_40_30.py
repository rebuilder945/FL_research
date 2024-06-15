se1=input()
se2=input()
lst=["red","blue","yellow"]
if se1==se2 or (se1 not in lst) or (se2 not in lst):
    print("error")
if (se1==lst[0] and se2==lst[1]) or (se1==lst[1] and se2==lst[0]):
    print("purple")
if (se1==lst[0] and se2==lst[2]) or (se1==lst[2] and se2==lst[0]):
    print("orange")
if (se1==lst[2] and se2==lst[1]) or (se1==lst[1] and se2==lst[2]):
    print("green")

