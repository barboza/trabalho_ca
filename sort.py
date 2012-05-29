import random
import sys
import time
sys.path.append("./lib")

import bubble
import quick
import counting
import radix
import createCSV

def getSequence(size, min=0, max=100):
  sequence = []
  for i in range(size):
    sequence.append(random.randrange(min,max))  
  return sequence



table_bubble = [ [[],[],[],[],[],[]] for i in range(100) ]
table_quick = [ [[],[],[],[],[],[]] for i in range(100) ]


sequence = getSequence(50)

originalSequence = sequence[:]
print sequence
startTime = time.time()
sequence = radix.radix_sort(sequence,10)
print time.time()-startTime
print sequence


# startTime = time.time()

# print time.time()-startTime