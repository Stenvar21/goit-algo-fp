import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, level):
    if level == 0:
        return
    
    # Розраховуємо координати кінця гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малюємо лінію від початкової точки до кінцевої
    plt.plot([x, x_end], [y, y_end], color="brown", lw=2)

    # Рекурсивно малюємо ліву та праву гілки
    new_length = length * np.sqrt(2) / 2  # Зменшуємо довжину гілок
    new_angle_left = angle + np.pi / 4  # Ліва гілка на 45 градусів
    new_angle_right = angle - np.pi / 4  # Права гілка на -45 градусів

    # Рекурсія для лівої і правої гілок
    draw_tree(x_end, y_end, new_angle_left, new_length, level - 1)
    draw_tree(x_end, y_end, new_angle_right, new_length, level - 1)

def create_pythagoras_tree(level):
    plt.figure(figsize=(8, 8))
    plt.axis('equal')
  
    # Початкові координати (відправна точка)
    x_start, y_start = 0, 0
    initial_length = 1  # Початкова довжина стовбура
    initial_angle = np.pi / 2  # Початковий кут (90 градусів)

    # Викликаємо рекурсивну функцію для малювання дерева
    draw_tree(x_start, y_start, initial_angle, initial_length, level)

    # Показуємо результат
    plt.show()

level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))

create_pythagoras_tree(level)