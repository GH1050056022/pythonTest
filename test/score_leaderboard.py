from test.data_masking import data_masking



# 分数排行榜前三
def score_sore():
  trophy_info = {'1':{"user_name":"不问知雪","agency_name":"某某有限公司","score":1200},
                 '2':{"user_name":"不问知","agency_name":"某某有限公司","score":1000},
                 '3':{"user_name":"不问雪","agency_name":"某某有限公司","score":700},
                 '4':{"user_name":"不问","agency_name":"某某有限公司","score":1000}
                 }
  trophy_info =sorted(trophy_info.values(),key=lambda n: (n['score'],n['user_name']),reverse=True)
  if len(trophy_info) > 3:
    trophy_info = trophy_info[0:3]
  for info in trophy_info:
    info['user_name'] = data_masking(info['user_name'])
  print(trophy_info)

score_sore()