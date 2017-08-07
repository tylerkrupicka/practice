# RZero Matrix
# find zeroes and zero row and column

m = [[1, 0, 3, 4],[5, 6, 0, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

def print_matrix(m):
    for row in m:
        print(row)

def zero_matrix(m):
    zero_rows = {}
    zero_cols = {}
    for row in range(len(m)):
        for col in range(len(m)):
            if m[row][col] == 0:
                #found a zero
                zero_rows[row] = True
                zero_cols[col] = True
    for row in range(len(m)):
        for col in range(len(m)):
            if row in zero_rows or col in zero_cols:
                m[row][col] = 0
    return m

if __name__ == '__main__':
    print_matrix(m)
    print()
    n = zero_matrix(m)
    print_matrix(n)
