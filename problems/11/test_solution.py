from solution import load_grid, find_all_1d_arrays

def test_number_1d_arrays_simple_grid():
    grid = load_grid("simple_grid.csv")
    number_valid_arrays = len(find_all_1d_arrays(grid))
    assert number_valid_arrays == 10, "Expected 10 1-dimensional arrays"
