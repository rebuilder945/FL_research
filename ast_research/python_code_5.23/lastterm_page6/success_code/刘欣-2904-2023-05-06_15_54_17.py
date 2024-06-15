def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    num_str = str(a)
    for i in range(1, a+1):
        s += int(num_str * i)
        num_str += str(a)
    print(s)
main()

