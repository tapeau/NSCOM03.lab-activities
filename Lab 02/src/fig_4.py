import matplotlib.pyplot as plt

c = 1/2
N = 100000

r_values = range(1, 11)  # r from 1 to 10

S_values = [c * N * (1/r) for r in r_values]

plt.figure(figsize=(10, 6))
plt.plot(r_values, S_values, marker='o', linestyle='-', color='b')
plt.title('Baud Rate (S) vs. r')
plt.xlabel('r')
plt.ylabel('S (baud)')
plt.grid(True)
plt.xticks(r_values)
plt.yticks([c * N * (1/r) for r in r_values])
plt.xlim(0, 10)
plt.ylim(5000, 50000)
plt.show()