def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    lst=[a]
    b=a
    if a<10:
        for x in range(a-1):
            b=10*b+a
            lst.append(b)
    elif a>=10:
        for x in range(a-1):
            b=100*b+a
            lst.append(b)
    print(sum(lst))

main()

