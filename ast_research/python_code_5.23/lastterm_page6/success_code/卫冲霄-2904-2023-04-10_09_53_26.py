def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=str(a)
    ls=[]
    for i in range(1,a+1):
        num=b*i
        nums=int(num)
        ls.append(nums)
    print(sum(ls))
main()

