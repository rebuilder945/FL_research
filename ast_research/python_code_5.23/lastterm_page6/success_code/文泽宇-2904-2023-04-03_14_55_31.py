def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        lst = []
        shu = 0
        for i in range(1,a+1):
                shu = a * (10**(i - 1)) + shu
                lst.append(shu)
        print(sum(lst))
main()

