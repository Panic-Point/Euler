# Have to Recognize that this problem is just 2nCn. Use Scipy to do it easier.
import scipy.special

print(scipy.special.comb(40, 20, exact=True, repetition=False))
