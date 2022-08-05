#!/usr/bin/env python3
### Standard Packages ###
import os
import time
from uuid import uuid4 as uuid
from typing import List, Tuple

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
  data: DataFrame = read_csv('dress.csv') # Data from Kaggle, Fashion Dataset by nitinsss
  sample_size: int = 100
  
  primary_colors: List[Tuple[int, int, int]] = []
  secondary_colors: List[Tuple[int, int, int]] = []
  t1: float = time.time()

  ### Without Parallelization ###
  # for row in data[:sample_size].itertuples():
  #   primary, secondary = extract_image_colors(row.image_url)
  #   primary_colors.append(primary)
  #   secondary_colors.append(secondary)

  ### With Parallization ###
  for primary, secondary in Parallel(n_jobs=-1) \
    (delayed(extract_image_colors)(img_url) for img_url in data.image_url.values[:sample_size]):
    primary_colors.append(primary)
    secondary_colors.append(secondary)
  t2: float = time.time()
  print(f'Runtime: { t2 - t1 }')

if __name__ == '__main__':
  main()

