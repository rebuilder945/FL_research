b = []
def main():
    a = eval(input())
    if type(a) is int:
        b.append(a)
        main()
main()
print(len(b),end=" ")
print(sum(b))

