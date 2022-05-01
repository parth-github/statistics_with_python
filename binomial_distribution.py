'''
Example: if it is known that probability of passing 100 students in a class is .8
Problem: what's the probability of passing exactly 60 students from the class
n = 100
x = 60
p = 0.8
f(x=60) = fact(n)/ fact(x)*fact(n-x) * p**x * (1-p) ** (n-x)
'''
sample_size = 100
prob = 0.8

'''
def fact(z):
    if z <= 1: return 1
    return z * fact(z-1)

def binom_funct(n, x, p):
    return fact(n)/ fact(x)*fact(n-x) * (p**x) * ((1-p) ** (n-x))

binom_distrib = {}
for x in range(1, 101):
    binom_distrib.update({x: binom_funct(sample_size, x, prob)})
print(binom_distrib)

'''
from scipy.stats import binom
# setting the values
# of n and p
n = 100
p = 0.8
# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance 
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
binom_distrib_1 = {}
for x in range(n + 1):
    binom_distrib_1.update({x: binom.pmf(x, n, p)})
# printing the table
print("r\tp(r)")
for i in range(n + 1):
    print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))


import matplotlib.pyplot as plt

x2points = binom_distrib_1.keys()
y2points = binom_distrib_1.values()

plt.plot(x2points, y2points, marker='o')
plt.xlabel('Event of passing exactly x number of students')
plt.ylabel('Probability of students passing, f(x): PMF')
plt.title('Binomial Distirbution: Passing Students')
plt.show()
