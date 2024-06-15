def shift(lst):
       lst=eval(input())
       b=lst
       f=lst[-1]
       for x in range(lst-1):
            b[x+1]=lst[x]
       b[0]=f
       print(b)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

