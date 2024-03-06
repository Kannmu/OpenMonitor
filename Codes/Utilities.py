
import multiprocessing
multiprocessing.freeze_support()
def sort_matrix_by_row(matrix, row_index):
    matrix[row_index] = [float(i) for i in matrix[row_index]]
    sorted_data = [
        list(x)
        for x in zip(*sorted(zip(*matrix), key=lambda x: x[row_index], reverse=True))
    ]
    return sorted_data