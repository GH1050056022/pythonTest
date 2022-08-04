import datetime


def get_month_of_year():
  # 2022_08
  current_year = datetime.datetime.now().year
  current_month = datetime.datetime.now().month
  current_year_month = str(current_year) + '_' + str(current_month).zfill(2)
  print(current_year_month)


get_month_of_year()