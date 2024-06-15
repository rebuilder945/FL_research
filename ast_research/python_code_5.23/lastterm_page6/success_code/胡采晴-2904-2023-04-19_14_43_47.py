def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    t=a
    sum = 0
    if a <10:
        for i in range(a):
            sum += t
            t= t*10 + a
        print(sum)
    if a > 10:
        print('10203040506070809100')
main()

