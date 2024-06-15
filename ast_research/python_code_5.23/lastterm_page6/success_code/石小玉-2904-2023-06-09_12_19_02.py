def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=a
        i=1
        nums=[a]
        while b>=i:
                a=a+a*(10**i)
                nums.append(a)
                i=i+1
        print(sum(nums))

main()

