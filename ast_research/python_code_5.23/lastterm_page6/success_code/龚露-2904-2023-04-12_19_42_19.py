def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    nums = []
    i = 0
    while i < a:
        x = str(a)*(i+1)
        nums.append(x)
        x = x+1
    print(sum(nums))

main()

