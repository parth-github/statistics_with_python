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
# fx = nCr * p**r * (1-p)**r

def fact(z):
    if z <= 1: return 1
    return z * fact(z-1)



import matplotlib.pyplot as plt

xpoints = freq_distrib.keys()
ypoints = freq_distrib.values()
plt.plot(xpoints, ypoints, marker='o')
plt.xlabel('Random Variable, X')
plt.ylabel('Frequency, f')
plt.title('Frequency Distirbution')
plt.show()

