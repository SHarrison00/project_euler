import argparse
import numpy as np

def load_grid(pathname):
    """Return a NumPy array for a given path name."""

    grid = np.genfromtxt(
        pathname, 
        delimiter=",", 
        dtype=int, 
        encoding="utf-8-sig"
    )

    assert len(grid.shape) == 2, "Grid expected to be 2-dimensional"
    assert grid.shape[0] == grid.shape[1], "Grid expected to be square"    
    assert grid.size >= 4, "Grid too small to contain any valid subarrays"

    return grid


def find_all_1d_arrays(grid):
    """Return list of all 1D arrays for a given grid."""

    n = grid.shape[0]

    horz_arrays = [row for row in grid]    
    vert_arrays = [grid[:,i] for i in range(0,n)]
    diag_array = [np.diagonal(grid, i) for i in range(-n+4, n-3)]
    anti_diag_arrays = [np.fliplr(grid).diagonal(i) for i in range(-n+4, n-3)]

    all_arrays = horz_arrays + vert_arrays + diag_array + anti_diag_arrays
    
    assert min([len(all_arrays[i]) for i in range(0,len(all_arrays))]) >= 4, \
        "Found an invalid array: too short (length < 4)"
        
    return all_arrays


def max_subarray_prod(arrays):
    """
    Compute the maximum product of any four consecutive values found from a 
    given list of 1D arrays using a modification of Kadane's algorithm.
    """
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("grid_path")
    args = parser.parse_args()
    
    grid = load_grid(args.grid_path)
    find_all_1d_arrays(grid)


if __name__ == "__main__":
    main()

"""

Example Usage:

- python solution.py simple_grid.csv
- python solution.py problem_grid.csv

"""