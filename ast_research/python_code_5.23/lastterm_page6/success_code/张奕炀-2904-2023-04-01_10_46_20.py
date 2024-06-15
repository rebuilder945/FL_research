def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    list0 = []
    for i in range(a):
        for s in range(i+1):
             list0.append(a * pow(10,s))
    sum0 = sum(list0)
    print(sum0)
main()

