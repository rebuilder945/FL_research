b = []
def main():
    a = input()
    if a != "#":
        b.append(eval(a))
        main()
main()
print(len(b),end=" ")
print(sum(b))

