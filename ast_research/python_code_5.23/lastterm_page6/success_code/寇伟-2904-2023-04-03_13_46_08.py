def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ls=[]
    for i in range(1,a+1):
        ls.append(a*10**(i))
    print(sum(ls))
main()

