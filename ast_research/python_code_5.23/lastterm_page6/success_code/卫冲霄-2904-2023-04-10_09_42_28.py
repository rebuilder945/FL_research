def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=str(a)
    nums=0
    for i in range(1,a+1):
        num=b*i
        nums=int(num)
        nums+=nums
    print(nums)
main()

