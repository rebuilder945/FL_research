def main():
    num = eval(input())
    calculate_e(num)
def calculate_sum(a):
        lst=[]
        for i in range(a):
            b=int(str(a)*(i+1))
            lst.append(b)
        print(sum(lst))

main()


