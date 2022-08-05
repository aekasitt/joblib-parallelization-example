#!/usr/bin/env python3
### Standard Packages ###
import os
import time
from argparse import ArgumentParser, Namespace
from typing import List, Tuple
from uuid import uuid4 as uuid

### Third-Party Packages ###
import httpx
from colorthief import ColorThief
from joblib import Parallel, delayed
from pandas import DataFrame, read_csv

def extract_image_colors(url: str) -> Tuple[Tuple[int, int, int], Tuple[int, int, int]]:
  unique_id: str = uuid()
  with open(f'{unique_id}.jpg', 'wb') as f:
    f.write(httpx.get(url).content)
  color_thief: ColorThief = ColorThief(f'{unique_id}.jpg')
  palette: tuple = color_thief.get_palette(color_count=2)
  os.remove(f'{unique_id}.jpg')
  return palette[0], palette[1]

def main():
  ### Parse arguments ##
  parser: ArgumentParser = ArgumentParser()
  parser.add_argument('--parallel', '-p', action='store_true', help='Run in parallel if flag enabled')
  parser.add_argument('--jobs', '-j', type=int, default=-1, help='Number of jobs to run in parallel')
  args: Namespace = parser.parse_args()

  ### Load dataset ###
  data: DataFrame = read_csv('dress.csv') # Data from Kaggle, Fashion Dataset by nitinsss
  sample_size: int = 100
  
  primary_colors: List[Tuple[int, int, int]] = []
  secondary_colors: List[Tuple[int, int, int]] = []
  t1: float = time.time()

  if args.parallel:
    ### With Parallization ###
    for primary, secondary in Parallel(n_jobs=args.jobs) \
      (delayed(extract_image_colors)(img_url) for img_url in data.image_url.values[:sample_size]):
      primary_colors.append(primary)
      secondary_colors.append(secondary)
  else:
    ### Without Parallelization ###
    for row in data[:sample_size].itertuples():
      primary, secondary = extract_image_colors(row.image_url)
      primary_colors.append(primary)
      secondary_colors.append(secondary)

  t2: float = time.time()
  print(f'Runtime: { t2 - t1 }')

if __name__ == '__main__':
  main()

