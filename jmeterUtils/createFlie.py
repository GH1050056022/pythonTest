import os
import datetime


def runTestPlan(path):
  # py 自动执行jmeter测试计划
  # 年-月-日 时：分：秒
  now_time = datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")
  print(now_time)
  path = path + "\\" + now_time

  result = path + "\\result"
  webreport = path + "\\webreport"

  createFile(result)
  createFile(webreport)
  os.system(
      "jmeter -n -t test.jmx -l " + now_time +
      "/result/result.txt -e -o " + now_time + "/webreport")


def createFile(foldername):
  # 文件路径
  word_name = os.path.exists(foldername)
  # 判断文件是否存在：不存在创建
  if not word_name:
    os.makedirs(foldername)


if __name__ == '__main__':
  path = r'C:\space\program\apache-jmeter-5.5\test'  # 文件夹建立位置
  runTestPlan(path)
