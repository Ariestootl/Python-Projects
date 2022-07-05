"""
Counting Letters in DNA Strings

Given some string dna containing the letters A, C, G, or T, representing the bases
that make up DNA, we ask the question: how many times does a certain base occur
in the DNA string? For example, if dna is ATGGCATTA and we ask how many
times the base A occur in this string, the answer is 3.
A general Python implementation answering this problem can be done in many
ways. Several possible solutions are presented below.
"""

def count_v1(dna, base):
    dna = list(dna)
    i = 0
    for x in dna:
        if x == base:
            i = i + 1
    return i

def count_v2(dna, base):
    i = 0
    for c in dna:
        if c == base:
            i += 1
    return i

def count_v3(dna, base):
    i = 0
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1
    return i

def count_v4(dna, base):
    i = 0
    j = 0
    while j < len(dna):
        if dna[j] == base:
            i += 1
        j += 1
    return i

def count_v5(dna, base):
    m = []
    for c in dna:
        if c == base:
            m.append(True)
        else:
            m.append(False)
    return sum(m)



"""
Extracting indices Instead of making a boolean list with elements expressing
whether a letter matches the given base or not, we may collect all the indices of the
matches. This can be done by adding an if test to the list comprehension:
"""
dna = "AATGCTTA"
base = "A"

indices = [i for i in range(len(dna)) if dna[i] == base]

indices

print(dna[0], dna[1], dna[7])
# ------------------------------------------------------------------------------------

"""
Generating random DNA strings The simplest way of generating a long string is
to repeat a character a large number of times:
"""


import random

def generate_string(N, alphabet="ATGCB"):
    return "".join([random.choice(alphabet) for i in range(N)])


dna = generate_string(1000)
print(dna)

print(count_v2(dna, "C"))


import time

functions = [count_v1, count_v2, count_v3, count_v4, count_v5]
timings = []

for function in functions:
    t0 = time.process_time()
    function(dna, "A")
    t1 = time.process_time()
    cpu_time = t1 - t0
    timings.append(cpu_time)

print(timings)
