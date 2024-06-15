def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    print(sum(int("".join([str(a)*i])))
    for i in range(1,a+1)
main()

