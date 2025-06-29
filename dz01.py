class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Функція реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Алгоритм сортування вставками для однозв'язного списку
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_list

    # Об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        if not list1.head:
            return list2
        if not list2.head:
            return list1

        # Знаходимо перший елемент об'єднаного списку
        if list1.head.data <= list2.head.data:
            merged_head = list1.head
            list1.head = list1.head.next
        else:
            merged_head = list2.head
            list2.head = list2.head.next

        current = merged_head
        while list1.head and list2.head:
            if list1.head.data <= list2.head.data:
                current.next = list1.head
                list1.head = list1.head.next
            else:
                current.next = list2.head
                list2.head = list2.head.next
            current = current.next

        # Якщо залишилися елементи в одному з списків
        if list1.head:
            current.next = list1.head
        if list2.head:
            current.next = list2.head

        merged_list = LinkedList()
        merged_list.head = merged_head
        return merged_list


# Приклад використання

llist1 = LinkedList()
llist1.insert_at_end(5)
llist1.insert_at_end(10)
llist1.insert_at_end(15)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(8)
llist2.insert_at_end(12)

print("Список 1:")
llist1.print_list()
print("Список 2:")
llist2.print_list()

# Сортуємо список 1
llist1.insertion_sort()
print("\nСписок 1 після сортування:")
llist1.print_list()

# Сортуємо список 2
llist2.insertion_sort()
print("\nСписок 2 після сортування:")
llist2.print_list()

# Об'єднуємо два відсортовані списки
merged_list = LinkedList.merge_sorted_lists(llist1, llist2)
print("\nОб'єднаний список:")
merged_list.print_list()

# Реверсуємо об'єднаний список
merged_list.reverse()
print("\nОб'єднаний список після реверсування:")
merged_list.print_list()