import getting_to_philosophy

urlRandom = 'http://en.wikipedia.org/wiki/Special:Random'
sum = 0

for x in range(1, 101):
  print("Test " + str(x))
  sum = sum + getting_to_philosophy.find_philosophy(urlRandom)

print("Average hops: " + str(sum / 100))