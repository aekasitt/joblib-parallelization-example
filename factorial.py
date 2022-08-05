#!/use/bin/env python3.8
import math
import time

from joblib import Parallel, delayed

def main():
  t1: float = time.time()

  ### Without parallelization ###
  #results: list = [math.factorial(x) for x in range(10_000)]
  
  ### With parallelization, as many cores as possible ###
  results: list = Parallel(n_jobs=-1)(delayed(math.factorial)(x) for x in range(10_000))  

  ### With parallelization ###
  # results: list = Parallel(n_jobs=2)(delayed(math.factorial)(x) for x in range(10_000))
  t2: float = time.time()
  print(f'Runtime: { t2 -t1 }')

if __name__ == '__main__':
  main()

