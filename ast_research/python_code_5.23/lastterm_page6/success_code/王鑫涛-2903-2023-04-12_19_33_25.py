def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m=1
    n = 1
    l=[1]
    if m <= num:
         n*=m
         l.append(1/n)
         m+=1
    print('%.6f'%sum(num))
main()


