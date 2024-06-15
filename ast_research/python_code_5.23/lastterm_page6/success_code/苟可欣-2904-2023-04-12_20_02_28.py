def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    lst=[a]
    b=a
    for x in range(a-2):
        b=10*b+a
        lst.append(b)
    print(sum(lst))

main()

