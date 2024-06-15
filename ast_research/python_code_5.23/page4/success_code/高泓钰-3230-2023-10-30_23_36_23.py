lst=eval(input())
lst.sort(reverse=True)
for x in lst:
    if x!=0:
        print(''.join(str(i)for i in lst ))
        break
    else:
        print("0")
        break

