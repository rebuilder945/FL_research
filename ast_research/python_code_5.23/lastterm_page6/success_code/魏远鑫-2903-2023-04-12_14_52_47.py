def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    c=1
    ls=[]
    for i in range(1,x+1):
        c*=i
        ls.append(c)
        b=len(ls)
        e=1
        ls2=[]
        for i in range(b):
                e+=1/(ls[i])
                ls2.append(e)
    print("%.6f"%ls2[-1])
main()


