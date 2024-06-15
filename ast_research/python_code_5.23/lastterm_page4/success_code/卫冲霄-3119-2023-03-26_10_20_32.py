ls=eval(input())
def remove_ls(ls):
    for i in ls:
        if ls.count(i)>1:
            ls.remove(i)
            remove_ls(ls)
    return ls
print(remove_ls(ls))

