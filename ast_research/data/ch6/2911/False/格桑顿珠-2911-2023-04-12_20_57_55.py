def  shift(lst):
    lst.insert(0,lst.pop())
    return lst
list1  =  input().split(",") 
shift(list1)
print(list1)
