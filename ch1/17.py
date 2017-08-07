# Rotate Matrix
# NxN matrix rotate 90 degrees

m = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]

def print_matrix(m):
    for row in m:
        print(row)

def rotate_matrix(m):
    # create new matrix
    n = []
    for i in range(len(m)):
        n.append([])
        for j in range(len(m)):
            n[i].append(0)
    # rotate_matrix
    i = len(m) - 1
    for row in m:
        for j in range(len(row)):
            n[j][i] = row[j]
        i -= 1
    return n

if __name__ == '__main__':
    print_matrix(m)
    print_matrix(rotate_matrix(m))
