from math import log

def getDigit(num, base, digit_num):
  return (num // base ** digit_num) % base

def makeBlanks(size):
  return [ [] for i in range(size) ]

def split(sequence, base, digit_num):
  buckets = makeBlanks(base)
  for num in sequence:
    buckets[getDigit(num, base, digit_num)].append(num)
  return buckets

def merge(sequence):
  newSequence = []
  for subSequence in sequence:
    newSequence.extend(subSequence)
  return newSequence

def maxAbs(sequence):
  return max(abs(num) for num in sequence)

def radix_sort(sequence, base):
  passes = int(log(maxAbs(sequence), base) + 1)
  newSequence = list(sequence)
  for digits_num in range(passes):
    newSequence = merge(split(newSequence, base, digits_num))
  return newSequence