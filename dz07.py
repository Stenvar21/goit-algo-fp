import random
import matplotlib.pyplot as plt
import pandas as pd

# Симуляція кидання двох кубиків
def simulate_dice_rolls(num_rolls):
    results = {sum_: 0 for sum_ in range(2, 13)}  # Ініціалізація результатів для кожної можливої суми
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)  # Кидок першого кубика
        roll2 = random.randint(1, 6)  # Кидок другого кубика
        total = roll1 + roll2  # Сума результатів
        results[total] += 1  # Збільшуємо лічильник для цієї суми
    
    # Обчислення ймовірностей
    probabilities = {key: value / num_rolls * 100 for key, value in results.items()}
    return probabilities

# Аналітичні ймовірності для двох кубиків
analytical_probabilities = {
    2: 1/36 * 100, 3: 2/36 * 100, 4: 3/36 * 100, 5: 4/36 * 100, 6: 5/36 * 100,
    7: 6/36 * 100, 8: 5/36 * 100, 9: 4/36 * 100, 10: 3/36 * 100, 11: 2/36 * 100, 12: 1/36 * 100
}

# Виконуємо симуляцію Монте-Карло
num_rolls = 10000
monte_carlo_probabilities = simulate_dice_rolls(num_rolls)

# Створюємо таблицю для виведення результатів
data = {
    "Сума": list(range(2, 13)),
    "Ймовірність (Метод Монте-Карло)": [monte_carlo_probabilities[i] for i in range(2, 13)],
    "Ймовірність (Аналітична)": [analytical_probabilities[i] for i in range(2, 13)]
}

df = pd.DataFrame(data)

# Виведення таблиці
print(df)

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.bar(df['Сума'] - 0.2, df['Ймовірність (Метод Монте-Карло)'], width=0.4, label='Монте-Карло', align='center')
plt.bar(df['Сума'] + 0.2, df['Ймовірність (Аналітична)'], width=0.4, label='Аналітична', align='center')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Порівняння ймовірностей (Метод Монте-Карло vs Аналітичні розрахунки)')
plt.legend()
plt.xticks(range(2, 13))
plt.show()
