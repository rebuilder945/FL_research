def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    nums=[]
    i = 1
    while i < a:
        x = str(a)*i
        nums.append(int(x))
        i = i + 1
    print(sum(nums))
main()

