from collections import defaultdict

def counting_sort(sequence, min, max):
  count = defaultdict(int)

  for i in sequence:
    count[i] += 1
  result = []
  for j in range(min,max+1):
    result += [j]* count[j]
  return result