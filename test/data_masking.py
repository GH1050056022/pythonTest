# -*- coding: utf-8 -*-


def data_masking(var):
  # null return
  if not var :
    return var
  var = var.strip()
  count = len(var)
  if count <= 2:
    var = var[0] + '*'
  else:
    if count < 11:
      var = var[0] + '*'*(len(var)-2) + var[count - 1]
    else:
      var = var[0] + '*'*9 + var[count - 1]
  return var

var = data_masking(' Tommy Wong ')
print(var)