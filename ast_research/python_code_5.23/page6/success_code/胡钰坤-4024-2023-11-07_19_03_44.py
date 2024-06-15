def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    lst = []
    for i in range(a):
        s = int(str(a)*(i+1))
        lst.append(s)
    print(sum(lst))
main()

