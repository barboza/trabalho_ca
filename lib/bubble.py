def bubble_sort(sequence):

  changed = True

  while changed:
    changed = False
    for i in xrange(len(sequence) - 1):
      if sequence[i] > sequence[i+1]:
        sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
        changed = True

  return None
