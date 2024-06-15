lst = list(map(int, input().split(',')))  
n, m = map(int, input().split(','))  
if n >= 0 and n < len(lst) and m >= 0 and m < len(lst):  
    lst = lst[:n] + lst[n+1:m] + lst[m+1:]
    print(lst) 
else:  
    print("error")  
