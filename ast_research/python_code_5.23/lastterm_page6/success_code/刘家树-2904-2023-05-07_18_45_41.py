def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    nums =0
    i=0
    while i<a :
        x=str(a)*(i+1)
        nums.append(int(x))
        i=i+1
    print(sum(nums))
main()

