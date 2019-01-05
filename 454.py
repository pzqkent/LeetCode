def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)

  # collection.Counters provide you a dict which map the value to frequency. 
  # That is, AB[-c-d] means the frequency of (a+b=-c-d)