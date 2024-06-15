def shift(lst):
def main():
    total_count=int(input())
    i=0
    while total_count > 0:
        total_count-=int(total_count/2)+2
        i=i+1
    print(i)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

