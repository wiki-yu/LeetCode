
# 1. Computational Complexity
We can consider the time complexity and space complexity. (Big-O notation)
# 2. Time Complexity
## 2.1 Constant Time — O(1)
```python
if a > b:
    return True
else:
    return False
```
An algorithm is said to have a constant time when it is not dependent on the input data (n).
## 2.2 Logarithmic Time — O(log n)
Algorithms with logarithmic time complexity are commonly found in operations on binary trees or when using binary search.
## 2.3 Linear Time — O(n)
An algorithm is said to have a linear time complexity when the running time increases at most linearly with the size of the input data.
## 2.4 Quasilinear Time — O(n log n)
An algorithm is said to have a quasilinear time complexity when each operation in the input data have a logarithm time complexity. It is commonly seen in sorting algorithms (e.g. mergesort, timsort, heapsort).
## 2.5 Quadratic Time — O(n²)
An algorithm is said to have a quadratic time complexity when it needs to perform a linear time operation for each value in the input data, for example:
```python
for x in data:
    for y in data:
        print(x, y)
```
## 2.6 Exponential Time — O(2^n)
An algorithm is said to have an exponential time complexity when the growth doubles with each addition to the input data set. This kind of time complexity is usually seen in brute-force algorithms

# 3. Space Complexity
Reference Link: https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7


