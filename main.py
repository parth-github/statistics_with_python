num = [[1, 2], [3, 4], [4, 5, 3]]

numMap = list(map(lambda x: x + [1], num))
print(numMap)
flatMap = [val for elem in numMap for val in elem]
print(flatMap)
#numFlat = flatmap(lambda x: x, numMap)
#print(list(numFlat))

print(flatMap.count(1))

### statistics
'''
create a random variable with a list

'''
rand_var = flatMap
print(f'Values of Random Variable = {rand_var}')
sample_size = len(rand_var)
print(f'Sample Size = {sample_size}')
sample_space = []
sample_space_set = set(rand_var)
sample_space = list(sample_space_set)
print(f'Sample Space = {sample_space_set}')
freq_distrib = {}

for x in rand_var:
    if x not in freq_distrib.keys():
        freq_distrib.update({x: 0})
    freq_distrib[x] = freq_distrib[x] + 1
print(freq_distrib)


prob_distrib = {}

for x, freq in freq_distrib.items():
    prob_distrib.update({x : freq/sample_size})

print(f'Probability Distribution: {prob_distrib}')

# Binomial Distribution
# fx = nCx * p**x * (1-p)** (n-x)
'''
Example: if it is known that probability of passing 100 students in a class is .8
Problem: what's the probability of passing exactly 60 students from the class
n = 100
x = 60
p = 0.8
f(x=60) = fact(n)/ fact(x)*fact(n-x) * p**x * (1-p) ** (n-x)
'''
def fact(z):
    if z <= 1: return 1
    return z * fact(z-1)

def binom_funct(n, x, p):
    return fact(n)/ fact(x)*fact(n-x) * p**x * (1-p) ** (n-x)

binom_distrib = {}
for x, prob in prob_distrib.items():
    binom_distrib.update({x: binom_funct(sample_size, x, prob)})
print(binom_distrib)

import matplotlib.pyplot as plt

x1points = freq_distrib.keys()
y1points = freq_distrib.values()
plt.title('Distribution')
plt.subplot(2,1,1)
plt.plot(x1points, y1points, marker='o')
plt.xlabel('Random Variable, X')
plt.ylabel('Frequency, f')
plt.suptitle('Frequency Distirbution')

x2points = binom_distrib.keys()
y2points = binom_distrib.values()
plt.subplot(2,1,2)
plt.plot(x2points, y2points, marker='+')
plt.xlabel('Event of passing X number of students')
plt.ylabel('Probability, f(x)')
plt.suptitle('Binomial Distirbution')
plt.show()
