from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def find_low(num):
  digits = get_digits(increase(num))
  digits.sort()
  return int(''.join(digits))

def find_high(num):
  digits = get_digits(increase(num))
  digits.sort()
  digits.reverse()
  return int(''.join(digits))

def increase(num):
  while (num < 1000):
    num *= 10
  return num

def get_digits(num):
  return [i for i in str(num)]

KAPREKAR_NUM = 6174
counts = np.zeros(9000)
hist = defaultdict(lambda: 0)
for i in range(1000,10000):
  if (i % 1111 == 0):
    continue
  diff, count = i, 0
  while (diff != KAPREKAR_NUM):
    diff = find_high(diff) - find_low(diff)
    count += 1
  counts[1000-i] = count

plt.hist(counts, 7, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Iterations to Kaprekar Number')
plt.ylabel('Frequency')
#plt.bar(hist.keys(), hist.values(), 2.0, color='g')
plt.show()
