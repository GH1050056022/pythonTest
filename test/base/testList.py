# 列表

list1 = ['Google', 'Lucio', 1997, 2000]
# del可以删掉一个元素
del list1[0]
# 删除指定内容
list1.remove('Lucio')
# 添加元素
list1.append('alibaba')
print("删除列表项后的list1: %s", list1)
# 列表元素个数
len(list1)
# 列表最大值
list1.reverse()
# 复制
list2 = list1.copy()
print("list1: %s", list1)
print("list2: %s", list2)
# 清空
list2.clear()
print("list2.clear(): %s", list2)

