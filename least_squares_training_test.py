import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def extract_features_response(input_file):
    x = []
    y = []
    for line in input_file:
        #print(f"line = {line}")
        line_clean = list(map(lambda x: int(x), line.split()))
        #print(f"line clean = {line_clean}")
        if line_clean:
            y.append(line_clean[-1])
            x.append(line_clean[:-1])
    return (x,y)

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading

    # read in the training data and separate it to x_train and y_train
    x_train, y_train = extract_features_response(StringIO(train_string))
     
    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train)[0]

    # read in the test data and separate x_test from it
    x_test, y_test = extract_features_response(StringIO(test_string))

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
