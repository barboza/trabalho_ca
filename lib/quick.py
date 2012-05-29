from random import randrange

def quick_sort(sequence):
  less = []
  pivotList = []
  more = []

  if len(sequence) <= 1:
    return sequence
  else:
    pivot = sequence[randrange(0,len(sequence))]
    for i in sequence:
      if i < pivot:
        less.append(i)
      elif i > pivot:
        more.append(i)
      else:
        pivotList.append(i)
    less = quick_sort(less)
    more = quick_sort(more)
    return less + pivotList + more 
