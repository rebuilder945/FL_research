lst=eval(input())
lst = [int(x) for x in lst]
lst.sort(reverse=True)
result = int(''.join(str(x) for x in lst))
print(result)
