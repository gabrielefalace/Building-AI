import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading

def extract_features_response(input_file):
    #print("input file: \n")
    #print(input_file)
    x = []
    y = []
    for line in input_file:
        line_clean = list(map(lambda x: int(x), line.split()))
        #print(f"line = {line_clean}")
        if line_clean:
            y.append(line_clean[-1])
            x.append(line_clean[:-1])
    return (x,y)

def fit_model(input_file):

    x, y = extract_features_response(input_file)

    c = np.linalg.lstsq(x, y)[0]

    print(c)
    print(x @ c)

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
