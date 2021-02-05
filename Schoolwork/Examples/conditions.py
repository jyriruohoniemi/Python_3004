aapeli = 10
beebeli = 10

if aapeli > beebeli:
 print("aapeli on isompi")
else:
  print("nyt ollaan fakissa")

if beebeli > aapeli:
 print("beebeli on isompi")

start = 0
end = 10
while start <= end:
    start += 1
    if start % 2 != 0:
        continue
    print(start)