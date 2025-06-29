import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random

# Клас вузла бінарного дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"  # Чорний колір за замовчуванням
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Додавання ребер у граф для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використовуємо id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуємо значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для генерації кольорів у форматі RGB для кожного вузла
def generate_color(index, total_nodes):
    # Генерація кольору на основі індексу для кожного вузла
    r = int(255 * (index / total_nodes))
    g = int(255 * (1 - (index / total_nodes)))
    b = random.randint(0, 255)
    return f'#{r:02X}{g:02X}{b:02X}'

# Обхід у глибину (DFS) за допомогою стеку
def dfs(tree_root):
    stack = [tree_root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            node.color = generate_color(len(visited), len(visited))  # Зміна кольору вузла залежно від порядку обходу
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited

# Обхід в ширину (BFS) за допомогою черги
def bfs(tree_root):
    queue = [tree_root]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            node.color = generate_color(len(visited), len(visited))  # Зміна кольору вузла залежно від порядку обходу
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited

# Створення дерева
root = Node(0)
root.left = Node(3)
root.left.left = Node(4)
root.left.right = Node(12)
root.right = Node(1)
root.right.left = Node(2)

# Виконання обох обходів і візуалізація
print("DFS обхід:")
dfs(root)
draw_tree(root)

print("BFS обхід:")
bfs(root)
draw_tree(root)