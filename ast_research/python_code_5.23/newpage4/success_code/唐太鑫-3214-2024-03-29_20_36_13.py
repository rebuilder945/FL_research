lst=eval(input())
a=lst.count("0")
while a > 0:
    lst.remove("0")
lst1=["0"]*a
lst=lst+lst1
print(lst)

