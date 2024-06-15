def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    ls=[1]
    for i in range(1,num+1):
        ls.append(ls[-1]*1/i)
    e=sum(ls)
    print("%.6f"%e)

main()


