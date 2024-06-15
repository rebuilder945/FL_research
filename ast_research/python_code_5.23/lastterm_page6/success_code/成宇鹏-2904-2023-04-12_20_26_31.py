def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    lst = []
    for x in range(a):
        b = str(a)*(x+1)
        lst.append(int(b))
    print(sum(lst))
main()

