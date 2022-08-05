# Example repo for using Joblib

## Use parallelization to speed up runtime

* Example #1: `factorial.py`
  
  Without Parallelization
  ```sh
  python factorial.py
  $ Runtime: 12.571757078170776
  ```

  With Parallelization
  ```sh
  python factorial.py --parallel
  $ Runtime: 2.6366729736328125
  ```

  With Parallelization running two jobs
  ```sh
  python factorial.py --parallel --jobs 2
  $ Runtime: 6.87609601020813
  ```

* Example #2: `fashion.py`

  Before running this example, you must first download the [Kaggle Data](https://www.kaggle.com/datasets/nitinsss/fashion-dataset-with-over-15000-labelled-images?resource=download) and place on root folder as `dress.csv`
  
  Without Parallelization
  ```sh
  python fashion.py
  $ Runtime: 161.30089116096497
  ```

  With Parallelization
  ```sh
  python fashion.py --parallel
  $ Runtime: 20.59570002555847
  ```

  With Parallelization running two jobs
  ```sh
  python fashion.py --parallel --jobs 2
  $ Runtime: 79.21092510223389
  ```

