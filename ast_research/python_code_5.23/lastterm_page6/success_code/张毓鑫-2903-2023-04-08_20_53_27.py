def main():
    num = eval(input())
    calculate_e(num)
def jie(a):
        b=1
        for i in range(1,a+1):
            b/=i
        return b
def calculate_e(a):
        b=[]
        for i in range(1,a+1):
            c=jie(i)
            b.append(c)
        print(sum(b))
main()


