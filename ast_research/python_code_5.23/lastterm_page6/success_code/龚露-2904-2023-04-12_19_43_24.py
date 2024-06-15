def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    nums = []
    i = 0
    while i < a:
        x = str(a)*(i+1)
        y = int(x)
        nums.append(y)
        i = i+1
    print(sum(nums))

main()

