import threading
import time

class MyThread (threading.Thread):
  def __init__(self, threadID, name, delpay):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.delpay = delpay
  def run(self):
    print("开始线程" + self.name)
    # 获取锁
    threadLock.acquire()
    print_time(self.name, self.delpay, 3)
    print("释放锁，开启下一个线程")
    threadLock.release()

def print_time(threadName, delpay,  counter):
    while counter:
      time.sleep(delpay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, "Thread1", 1)
thread2 = MyThread(2, "Thread2", 2)

# 开启新线程
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程" )