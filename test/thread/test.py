import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delpay):
  count = 0
  while count < 5:
    time.sleep(delpay)
  count += 1
  print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
  _thread.start_new_thread(print_time, ("Thread1", 2))
  _thread.start_new_thread(print_time, ("Thread2", 4))
except:
  print("线程无法启动")

while 1:
  pass
