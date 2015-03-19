"""
Test pop speed
"""

from timeit import Timer

# Simple test #
###############

print("#########################")
print("Simple single speed test:")
print("")

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))

print("Pop first element takes", pop_zero.timeit(number=1000), "milliseconds")
print("Pop last element takes", pop_end.timeit(number=1000), "milliseconds")

# Loop test #
#############

print("")
print("##########")
print("Loop test:")
print("")

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

print("pop(0)   pop()")

for i in range(10**6, 10**7 + 1, 10**6):
    x = list(range(i))
    pt = pop_end.timeit(number=1000)
    pz = pop_zero.timeit(number=1000)
    print("%15.5f, %15.5f" % (pz, pt))

"""
pop() takes O(1) time
pop(i) takes O(n) time
"""