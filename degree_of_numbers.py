import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c='orange', edgecolors=None, s=50)

# Назначение заголовка диаграмы и меток осей.
plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of values', fontsize=14)

# Назначение шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)

# Назначение диапазона для каждой оси.
plt.axis([0, 6, 0, 60])

plt.show()
