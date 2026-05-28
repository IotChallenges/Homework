import matplotlib.pyplot as plt

r1 = [1, 2, 3, 4, 5, 6]
eta = [0.4072, 0.4167, 0.4467, 0.4533, 0.4426, 0.4226]

plt.figure(figsize=(6, 4))
plt.plot(r1, eta, marker='o')
plt.xlabel('Initial frame size $r_1$')
plt.ylabel('Efficiency $\\eta$')
plt.title('Efficiency over values of initial frame size')
plt.grid(True)
plt.xticks(r1)
plt.tight_layout()
plt.savefig('exercise3_efficiency.png', dpi=300)
plt.show()