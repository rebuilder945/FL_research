jack = ['1', '2', '3', '4', '5', '6', '1', '7', '7']
max_val = max(jack)
min_val = min(jack)
jack.remove(max_val)
jack.remove(min_val)
#从列表 jack 中删除最大值和最小值，但是 del 语句不能直接用于删除列表中的特定值，
#可以通过列表方法 remove() 来删除指定的值
print("jack list after del:", jack)