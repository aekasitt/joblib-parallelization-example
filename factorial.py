#!/use/bin/env python3.8
### Standard Packages ###
import math
import time
from argparse import ArgumentParser, Namespace

from joblib import Parallel, delayed

def main():
  parser: ArgumentParser = ArgumentParser()
  parser.add_argument('--parallel', '-p', action='store_true', help='Run in parallel if flag enabled')
  parser.add_argument('--jobs', '-j', type=int, default=-1, help='Number of parallel jobs')
  args: Namespace = parser.parse_args()

  results: list
  t1: float = time.time()

  if args.parallel:
    ### With parallelization ###
    results = Parallel(n_jobs=args.jobs)(delayed(math.factorial)(x) for x in range(10_000))  
  else:
    ### Without parallelization ###
    results = [math.factorial(x) for x in range(10_000)]
  
  t2: float = time.time()
  print(f'Runtime: { t2 -t1 }')

if __name__ == '__main__':
  main()

