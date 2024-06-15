def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=a
        i=2
        nums=[a]
        while b>=i:
                a=a+b*(10**(i-1))
                nums.append(a)
                i=i+1
        print(sum(nums))

main()

