import scipy.special
#the point of this file is to calculate the probability of certain events happening.
#inputs are: # OF TOTAL CARDS, # OF SUCCESSES, # OF ATTEMPTS
def prob(total, success, attempts, discover):
    fail = total - success
    #probability without the ability to repeat(aka discovering a minion
    if discover is True:
        output = 1 - scipy.special.comb(fail, attempts) / scipy.special.comb(total, attempts)
    else:
        output = 1 - (fail/total) ** attempts
    return output