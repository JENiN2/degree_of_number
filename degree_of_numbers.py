import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=50)

# Назначение заголовка диаграмы и меток осей.
plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of values', fontsize=14)

# Назначение шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)

plt.show()
