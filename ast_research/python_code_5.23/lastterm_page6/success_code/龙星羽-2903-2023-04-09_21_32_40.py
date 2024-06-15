def main():
    num = eval(input())
    calculate_e(num)
def    calculate_e(num):
    ls=[1]
    b=1
    for i in range(num):
        b=b/(i+1)
        ls.append(b)
    print(sum(ls))
main()


