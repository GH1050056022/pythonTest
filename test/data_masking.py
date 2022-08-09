# -*- coding: utf-8 -*-


def data_masking(var):
  # null return
  if not var :
    return var
  count = len(var)
  if count <= 2:
    var = var[0] + '*'
  else:
    var = var[0] + '*'*(len(var)-2) + var[count - 1]
  return var

var = data_masking('不问知雪呀')
print(var)