import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


class MaxHeap:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, key):
        new_node = Node(key)
        self.nodes.append(new_node)
        if not self.root:
            self.root = new_node
        else:
            self._heapify_up(len(self.nodes) - 1)

    def _heapify_up(self, index):
        current = index
        while current > 0:
            parent = (current - 1) // 2
            if self.nodes[current].val > self.nodes[parent].val:
                self.nodes[current], self.nodes[parent] = self.nodes[parent], self.nodes[current]
                current = parent
            else:
                break

    def build_heap(self, elements):
        for element in elements:
            self.insert(element)

        for i in range(len(self.nodes) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        size = len(self.nodes)
        current = index
        left_child = 2 * current + 1
        right_child = 2 * current + 2
        largest = current

        if left_child < size and self.nodes[left_child].val > self.nodes[largest].val:
            largest = left_child
        if right_child < size and self.nodes[right_child].val > self.nodes[largest].val:
            largest = right_child

        if largest != current:
            self.nodes[current], self.nodes[largest] = self.nodes[largest], self.nodes[current]
            self._heapify_down(largest)

    def visualize(self):
        self.root = self.nodes[0]  # Перша вершина — це корінь купи
        for i in range(1, len(self.nodes)):
            self._add_node(self.root, self.nodes[i])
        draw_tree(self.root)

    def _add_node(self, parent, node):
        if parent.left is None:
            parent.left = node
        elif parent.right is None:
            parent.right = node
        else:
            self._add_node(parent.left, node)


# Створення бінарної купи і візуалізація
heap = MaxHeap()
heap.build_heap([32, 21, 15, 12, 8, 5])
heap.visualize()