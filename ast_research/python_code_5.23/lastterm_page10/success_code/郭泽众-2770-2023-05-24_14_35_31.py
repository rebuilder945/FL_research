def compare(s1,s2):
    l1 = [x for x in s1]
    l2 = [x for x in s2]
    l1.sort()
    l2.sort()
    if l1 == l2:
        print('True')
    else:
        print('False')
str1 = input()
str2 = input()
compare(str1,str2)
