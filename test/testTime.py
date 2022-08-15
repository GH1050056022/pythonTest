import time
from datetime import datetime

times = time.mktime(datetime.now().timetuple())
time_order = int(times)
# 时间戳显示
print(time_order)