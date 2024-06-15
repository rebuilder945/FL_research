def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=''
    ls=[]
    for i in range(a):
        s+='a'
        ls.append(int(s))
    print(sum(ls))
main()

