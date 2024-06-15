def max_sort(lt):
    n=len(lt)
    for i in range(n-1):
        for j in range(n-1-i):
            if str(lt[j])+str(lt[j+1])<str(lt[j+1])+str(lt[j]):
    s =''
    for k in lt:
        s+=str(k)
    return int(s)
eval(input(lt))
print(max_sort(lt))

