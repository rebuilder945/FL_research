a = list(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0
list1 = ['0','1','2','3','4','5','6','7','8','9','10']
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in a:
    if i in list1:
        count1 += 1
    elif i in list2:
        count2 += 1
    elif i == ' ':
        count3 += 1
    else:
        count4 += 1
print(count2,count3,count1,count4)


