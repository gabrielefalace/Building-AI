import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

"""
Rolls the Dice 10 times. 
"""
def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

def bayes(sequence):
    odds = 1.0           # start with odds 1:1
    for roll in sequence:
        # likelyhood_ratio = P(observed_result|loaded) / P (observed_result|normal)
        likelyhood_ratio = p2[roll-1] / p1[roll-1] 
        odds = odds * likelyhood_ratio
        print("odds at round " + str(roll) + " is: " + str(odds))
    if odds > 1:        
        return True
    else:
        return False

sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
