import numpy as np

def generate(p1):
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

def count(seq):
    occurrences = 0
    for j in range(0, len(seq)-4):
        counter = 0
        if seq[j] == 1:
            for i in range(j, j+5):
                if seq[i] == 1:
                    counter = counter + 1
        if counter == 5:
            occurrences = occurrences + 1

    return occurrences
    
def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
