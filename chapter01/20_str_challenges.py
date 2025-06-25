# Challenge No1
# F
# aa
# ccc
# oooo
# rrrrr
# yyyyyy

message1 = "Factory"

for i in range(len(message1)):
  print(message1[i] * (i + 1))

# Challenge No2
# F*****
# aa****
# ccc***
# oooo**
# rrrrr*
# yyyyyy

for i in range(len(message1)):
  print(message1[i] * (i + 1), end = "*" * (len(message1) - i - 1))
  print()