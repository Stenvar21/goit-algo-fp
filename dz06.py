def greedy_algorithm(items, budget):
    # Обчислення співвідношення калорій до вартості для кожної страви
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:  # Якщо вартість страви не перевищує бюджет
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Ініціалізація масиву для динамічного програмування
    n = len(items)
    dp = [0] * (budget + 1)  # dp[i] буде зберігати максимальні калорії при бюджеті i
    item_selection = [[False] * n for _ in range(budget + 1)]  # Додатковий масив для відстеження вибору страв

    item_list = list(items.items())

    for i in range(n):
        item, details = item_list[i]
        cost = details["cost"]
        calories = details["calories"]
        
        # Проходимо бюджет від високого до низького, щоб уникнути повторного використання тієї ж страви
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget] < dp[current_budget - cost] + calories:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_selection[current_budget] = item_selection[current_budget - cost][:]  # Копіюємо попередній вибір
                item_selection[current_budget][i] = True  # Позначаємо, що ця страва вибрана

    selected_items = []
    total_cost = 0
    for i in range(n):
        if item_selection[budget][i]:
            selected_items.append(item_list[i][0])
            total_cost += item_list[i][1]["cost"]

    return selected_items, dp[budget], total_cost


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Жадібний алгоритм
selected_items_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items_greedy)
print("Сума калорій:", total_calories_greedy)
print("Вартість:", total_cost_greedy)

# Динамічне програмування
selected_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", selected_items_dp)
print("Сума калорій:", total_calories_dp)
print("Вартість:", total_cost_dp)