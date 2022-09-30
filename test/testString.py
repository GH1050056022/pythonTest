

var = 'lucio'
# 将第一个字母大写
print(var.capitalize())

# 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
print(var.isalpha())

# 如果字符串只包含数字则返回 True 否则返回 False..
print(var.isdigit())

# 截掉字符串左边的空格或指定字符。
print(var.lstrip('l'))

if var.find('Lucio'):
  print('s')
else:
  print('f')

# 返回字符串长度
num = len(var)
print(num)