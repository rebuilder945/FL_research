lst=eval(input())
for i in range(lst):
    if i == max(lst) and i == min(lst):
        lst.remove(i)
print(lst)

