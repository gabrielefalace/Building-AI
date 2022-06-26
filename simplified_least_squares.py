import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def compute_error(a, b):
    error = 0
    for i in range(len(a)):
        error = error + (a[i] - b[i])**2
    return error

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for i, coeff in enumerate(c):
        predicted_result = X @ coeff

        error = compute_error(y, predicted_result)
        #print(f"Error for {predicted_result} is {error}")

        if error < smallest_error:
            smallest_error = error
            best_index = i

        pass     # edit here: calculate the sum of squared error with coefficient set coeff and
                 # keep track of the one yielding the smallest squared error
    print("the best set is set %d" % best_index)



find_best(X, y, c)
