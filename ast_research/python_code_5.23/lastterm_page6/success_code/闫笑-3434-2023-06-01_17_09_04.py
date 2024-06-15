str1 = str(input())
str2 = str(input())
List1 = ["red", "blue", "yellow"]
List2 = ["red", "blue"]
List3 = ["red", "yellow"]
List4 = ["blue", "yellow"]
if str1 == str2 or str1 not in List1 or str2 not in List1:
    print('error')
elif str1 in List2 and str2 in List2:
    print('purple')
elif str1 in List3 and str2 in List3:
    print('orange')
elif str1 in List4 and str2 in List4:
    print('green') 
