def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        ls=[]
        for i in range(1,a+1):
            a=str(a)
            ls.append(a*i)
        for i in range(len(ls)):
            ls[i]=int(ls[i])
        print(sum(ls))
main()

