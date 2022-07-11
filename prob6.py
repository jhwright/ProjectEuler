end = 101
s = 0
for i in range(end):
  r = sum(range(i+1,end))
  ir= i*r
  s += 2* ir 
  print(i, r, ir, s)