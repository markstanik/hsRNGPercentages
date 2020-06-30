import scipy.special
#the point of this file is to calculate the probability of certain events happening.
#inputs are: # OF TOTAL CARDS, # OF SUCCESSES, # OF ATTEMPTS
def prob(total, success, attempts):
    fail = total - success
    output = 1 - scipy.special.comb(fail, attempts) / scipy.special.comb(total, attempts)
    return output