def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ls = []
    for x in range(1,a+1):
        s = (a-x+1)*(a*10**(x-1))
        ls.append(s)
    print(sum(ls))
main()

