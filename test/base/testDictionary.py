# 字典在Python3中字典（dictionary ，简写为dict）是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 ( key=>value ) 对用冒号 (:) 分割，每个对之间用逗号 (,) 分割，
# 整个字典包括在花括号 ( {} ) 中


dict0 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = {'abc': 456, 'cde': 689}
dict2 = {'abc': 123, 98.6: 37}
# 删除键 'Beth'
del dict0['Beth']
# 删除字典
dict0.clear()
# 获得所有key
keys = dict2.keys()
# 获得所有value
values = dict2.values()
# 把dict2的值更新到dict1 的值中
dict1.update(dict2)
print(dict1)





