import random

def tq_iska_marsel():
    trialNum = 0
    heads_in_row = 0
    flips = 0
    while trialNum < 10000:
        heads_in_row = 0
        while heads_in_row < 3:
            if random.choice(["heads", "tails"]) == "heads":
                    heads_in_row = heads_in_row + 1
                    
            else:
                heads_in_row = 0
            flips = flips + 1
        trialNum = trialNum + 1
        avrage = int(flips/trialNum)
    return avrage
print(tq_iska_marsel())