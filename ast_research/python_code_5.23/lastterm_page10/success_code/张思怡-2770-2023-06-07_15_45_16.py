
def bwc(s1,s2):
    list1=list(s1)
    list2=list(s2)
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False

s1=input()
s2=input()
print(bwc(s1,s2))
