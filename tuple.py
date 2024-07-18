def last_(n): 
  return n[-1]

def sort_last(tuples):
  return sorted(tuples, key=last_)

#based on last digit
print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))