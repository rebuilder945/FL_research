lst1 = list(input())
lst3 = lst1.copy()
for x in range(len(lst1)):
    lst1[x] = (int(lst3[x])+5) % 10
lst2 = lst1.copy()
for i in range(int(len(lst1)/2)+1):
    lst1[i] = lst1[len(lst1)-1-i]
    lst1[len(lst1)-1-i] = lst2[i]
for m in lst1:
    print(m,end = "")

