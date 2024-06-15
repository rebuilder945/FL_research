def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    ls = []
    for i in range(x):
        b = int(str(x)*(i+1))
        ls.append(b)
    print(sum(lst))
main()

