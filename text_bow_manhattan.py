import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def manhattan_distance(data, i, j):
    row_i = data[i]
    row_j = data[j]
    distance = 0
    for k in range(len(data[i])):
        distance = distance + abs(row_i[k] - row_j[k])
    return distance


def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    
    for i in range(N):
        for j in range(N):
            # distance between row i and row j
            dist[i][j] = manhattan_distance(data, i, j)
    
    for i in range(N):
        dist[i][i] = np.inf

    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
