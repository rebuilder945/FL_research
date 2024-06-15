def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    i=1
    nums=[]
    while i <= a:
        s=int(str(a)*i)
        i=i+1
        nums.append(s)
    print(sum(nums))
main()

