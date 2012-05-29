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


MaxSize = 1000
Steps = 100

table_bubble = [ [[],[],[],[],[]] for i in range(Steps) ]
table_quick = [ [[],[],[],[],[]] for i in range(Steps) ]

for cicle in range(5):
  for size in range(Steps):
    realSize = MaxSize/Steps*size if MaxSize/Steps*size > 1 else 2 
    sequence = getSequence(realSize)
    
    bubbleSequence = sequence
    startTime = time.time()
    bubble.bubble_sort(bubbleSequence)
    endTime = time.time()
    table_bubble[size][cicle] = endTime - startTime

    quickSequence = sequence
    startTime = time.time()
    quick.quick_sort(quickSequence)
    endTime = time.time()
    table_quick[size][cicle] = endTime - startTime
    print size

createCSV.createCSV(table_bubble, "bubble")
createCSV.createCSV(table_quick, "quick")
