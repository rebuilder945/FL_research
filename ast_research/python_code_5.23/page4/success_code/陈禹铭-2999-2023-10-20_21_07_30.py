str_list=input().split( )
n,m=map(int,input().split())
if 0<=n<len(str_list) and 0<=m<len(str_list):
    str_list[n], str_list[m]=str_list[m],str_list[n]
    print(str_list)

