import random
import timeit

# random lists from [0-999] interval
print [random.randint(0,1000) for r in xrange(10)] # v1
print [random.choice([i for i in xrange(1000)]) for r in xrange(10)] # v2 