import matplotlib.pyplot as plt

get_x = int(input(f'Enter the length of the sequence: ')) + 1
get_y = int(input(f'Enter the degree: '))
x_values = list(range(1, get_x))
y_values = [x**get_y for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors=None, s=50)

# Назначение заголовка диаграмы и меток осей.
plt.title('Degree of numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Degree of values', fontsize=14)

# Назначение шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)

plt.show()
