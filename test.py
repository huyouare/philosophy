import getting_to_philosophy

urlRandom = 'http://en.wikipedia.org/wiki/Special:Random'
mySum = 0
count = 0

for x in range(1, 101):
  print("Test " + str(x))
  result = getting_to_philosophy.find_philosophy(urlRandom)
  if(result!=None):
    count = count + 1
    mySum = mySum + result

print("Average hops: " + str(mySum / count))