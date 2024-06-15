def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ls=[]
    for i in range(a):
        b=int(str(a)*(i+1))
    ls.append(b)
    print(sum(ls))
main()

