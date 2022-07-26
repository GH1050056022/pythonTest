import time  # 引入time模块
import calendar
print ("你好 世界！")
list =["a", "b", "c"]
print(list)


ticks = time.time()
print("当前时间戳为:", ticks)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
cal = calendar.month(2022, 7)
print("以下输出2022年7月份的日历:")
print(cal)

def function( str):
    print(str)
    return
function("调用函数")
#可写函数说明
def printinfo( name, age = 35 ):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return

#调用printinfo函数
printinfo( age=50, name="miki" )
printinfo( name="miki" )