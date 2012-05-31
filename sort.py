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
    sequence.append(long(random.randrange(min,max)))  
  return sequence

def getAvg(matrix):
  avg = []
  for i in matrix:
    avg.append(sum(i)/len(i))
  return avg

def getMax(matrix):
  maxValue = []
  for i in matrix:
    maxValue.append(max(i))
  return maxValue

def getMin(matrix):
  minValue = []
  for i in matrix:
    minValue.append(min(i))
  return minValue

def getArray(min_arr, avg_arr, max_arr):
  arr = []
  for i in range(len(min_arr)):
    arr.append(str(min_arr[i])+';'+str(avg_arr[i])+';'+str(max_arr[i]))
  return arr



def getMatrix(arrays, count):
  matrix = []
  for i in range(count):
    matrix.append([])
    for j in arrays:
      matrix[i].append(j[i])

  return matrix



MaxSize = 1000
Steps = 200

size_array = []

table_bubble = [ [[],[],[],[],[]] for i in range(Steps) ]
table_quick = [ [[],[],[],[],[]] for i in range(Steps) ]
table_counting_small = [ [[],[],[],[],[]] for i in range(Steps) ]
table_counting_large = [ [[],[],[],[],[]] for i in range(Steps) ]
table_radix = [ [[],[],[],[],[]] for i in range(Steps) ]

avg_bubble = []
avg_quick = []
avg_counting_small = []
avg_counting_large = []
avg_radix = []

min_bubble = []
min_quick = []
min_counting_small = []
min_counting_large = []
min_radix = []

max_bubble = []
max_quick = []
max_counting_small = []
max_counting_large = []
max_radix = []

#bubble-quick
for cicle in range(5):
  for size in range(Steps):
    realSize = MaxSize/Steps*size if MaxSize/Steps*size > 1 else 2 
    size_array.append(realSize)
    sequence = getSequence(realSize)
    
    bubbleSequence = sequence[:]
    startTime = time.time()
    bubble.bubble_sort(bubbleSequence)
    endTime = time.time()
    table_bubble[size][cicle] = endTime - startTime

    quickSequence = sequence[:]
    startTime = time.time()
    quick.quick_sort(quickSequence)
    endTime = time.time()
    table_quick[size][cicle] = endTime - startTime
    print size

print "done-quick/bubble"

#counting - k=3
for cicle in range(5):
  for size in range(Steps):
    realSize = MaxSize/Steps*size if MaxSize/Steps*size > 1 else 2 
    sequence = getSequence(realSize)

    countingSequence = sequence[:]
    startTime = time.time()
    counting.counting_sort(countingSequence,0,100)
    endTime = time.time()
    table_counting_small[size][cicle] = endTime - startTime
    print size

print "done-counting(3)"

#counting - k=10
for cicle in range(5):
  for size in range(Steps):
    realSize = MaxSize/Steps*size if MaxSize/Steps*size > 1 else 2 
    sequence = getSequence(realSize,0,100000)

    countingSequence = sequence[:]
    startTime = time.time()
    counting.counting_sort(countingSequence,0,100000)
    endTime = time.time()
    table_counting_large[size][cicle] = endTime - startTime
    print size

print "done-counting(8)"

#radix
for cicle in range(5):
  for size in range(Steps):
    realSize = MaxSize/Steps*size if MaxSize/Steps*size > 1 else 2 
    sequence = getSequence(realSize,0,100000)

    radixSequence = sequence[:]
    startTime = time.time()
    counting.counting_sort(countingSequence,0,100000)
    endTime = time.time()
    table_radix[size][cicle] = endTime - startTime
    print size

avg_bubble = getAvg(table_bubble)
avg_quick = getAvg(table_quick)
avg_counting_small = getAvg(table_counting_small)
avg_counting_large = getAvg(table_counting_large)
avg_radix = getAvg(table_radix)

min_bubble = getMin(table_bubble)
min_quick = getMin(table_quick)
min_counting_small = getMin(table_counting_small)
min_counting_large = getMin(table_counting_large)
min_radix = getMin(table_radix)

max_bubble = getMax(table_bubble)
max_quick = getMax(table_quick)
max_counting_small = getMax(table_counting_small)
max_counting_large = getMax(table_counting_large)
max_radix = getMax(table_radix)

arr_bubble = getArray(min_bubble,avg_bubble,max_bubble)
arr_quick = getArray(min_quick,avg_quick,max_quick)
arr_counting_small = getArray(min_counting_small,avg_counting_small,max_counting_small)
arr_counting_large = getArray(min_counting_large,avg_counting_large,max_counting_large)
arr_radix = getArray(min_radix,avg_radix,max_radix)

dataTable = getMatrix([size_array,arr_bubble,arr_quick,arr_counting_small,arr_counting_large,arr_radix],Steps)


createCSV.createCSV(dataTable, "data")

