str_list = input().split() 
n, m = map(int,input().split())  
str_list[n], str_list[m] = str_list[m], str_list[n]  
print(str_list)
