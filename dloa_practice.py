# print('gg')
# for i in range(5):
#     print(i)

import numpy as np 
a = np.random.randn(3,4,2)
b = np.random.randn(3,1,2)
c = np.random.randn(3,1,1)

d = c + a*b
print(d.shape)

init = np.random.randn(5000)
v1 = np.var(init)
init = 5 * init
v2 = np.var(init)

print(v1,v2)

distribution1 = np.random.normal(0.1, 3, 2000)
distribution2 = np.random.normal(-2, 1, 2000)
distribution3 = np.random.normal(3, 2, 2000)
distribution4 = np.random.normal(7, 2, 2000)

kwargs = dict(histtype = 'stepfilled', alpha = 0.3, normed = True, bins = 40)

import matplotlib.pyplot as plt

# plt.hist(distribution1, **kwargs)
# plt.hist(distribution2, **kwargs)
# plt.hist(distribution3, **kwargs)
# plt.hist(distribution4, **kwargs)

# plt.show()
# print(np.mean(distribution1))

print(np.argmax(np.array([[1,2,3,4],[1,2,3,4]]),0))


def draw_game_board(n):
    for i in range(n):
        print("*** " * (n-1)+'*')
        print("|  " * n + "|")
    print("*** " * (n-1) + "*")

draw_game_board(4)
# a = np.random.randint()


def reverse_integer(num):
    rev = 0
    while(num!=0):
        fig = num%10
        num = num//10
        rev = 10 * rev + fig
    return rev

print(reverse_integer(155))

def divisors(num):
    list_of_div = []
    for i in range(1,num+1):
        if num%i == 0:
            list_of_div.append(i)
    return list_of_div
print(divisors(122))

np.random.seed(0)
a = np.random.randint(100.0,size = 50)
print(a)
# a.astype(np.float64)

a = a.astype(float)
# a = np.array(a,dtype = float)
a = a.tolist()

list1 = []
list2 = []
print(a)
# print(type(a[0]))
# a = [1.0,2.0,3.0,4.0,5.0,6.0,7.0]

# for i, val in enumerate(a):
#     # print(i,val)
#     print(type(val))
for i, val in enumerate(a):
    if i % 2 == 0 and type(val) == float:
        list1.append(val)
        continue
    if i % 3 == 0 and type(val) == float:
        list2.append(val)


print(list1, list2)

def function1(text):
    return text == text[::-1]

print(function1('apple'))

A = '----'.join([' ',' ',' ',' ',' '])
B = '    '.join(['|','|','|','|','|'])
print('\n'.join([A,B,A,B,A,B,A,B,A]))


animals = {}
with open('label.txt') as f:
    line = f.readline()
    while line:
        if line in animals:
            animals[line] = animals[line] + 1
        else:
            animals[line] = 1
        line = f.readline()
print(animals)


def target_sum(input_list, target):
    length = len(input_list)
    if length <= 1:
        raise Exception("There's no solution")
    hash_map = dict()

    for i in range(length):
        if input_list[i] in hash_map:
            return [hash_map[input_list[i]],i]
        else:
            hash_map[target - input_list[i]] = i

print(target_sum([1,2,3,4,5,5,6,7,8],8))