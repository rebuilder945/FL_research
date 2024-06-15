def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        s=str(a)
        ls=[]
        for i in range(a):
                b=s*(i+1)
                ls.append(int(b))
        print(sum(ls))
main()

