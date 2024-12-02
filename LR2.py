import random
import matplotlib.pyplot as plt
import numpy as np

from BST import BST
from AVLTree import AVLTree
from RedBlackTree import RedBlackTree 

def generate_bst_and_plot_with_regression(n):
    """Генерация BST и построение графика зависимости высоты от числа элементов"""
    heights = []
    bst = BST()

    for i in range(1, n + 1):
        # Вставляем случайное число в диапазоне от 1 до 1000
        bst.insert(random.randint(1, 1000))
        heights.append(bst.height())

    x = np.arange(1, n + 1)
    y = np.array(heights)

    # Логарифмическая регрессия с основанием 2
    coeffs = np.polyfit(np.log2(x), y, 1)
    reg_curve = coeffs[0] * np.log2(x) + coeffs[1]

    print(f"Логарифмическая регрессия: h(n) = {coeffs[0]:.3f} * log2(n) + {coeffs[1]:.3f}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Фактическая высота")
    plt.plot(x, reg_curve, label="Регрессионная кривая", linestyle="--", color="orange")
    plt.xlabel("Количество ключей (n)")
    plt.ylabel("Высота дерева (h)")
    plt.title("Зависимость высоты бинарного дерева поиска от количества ключей")
    plt.legend()
    plt.grid(True)
    plt.show()

def generate_avl_and_plot_with_regression(n):
    """Генерация AVL дерева и построение графика зависимости высоты от числа элементов"""
    heights = []
    avl = AVLTree()

    for i in range(1, n + 1):
        avl.insert(i)
        heights.append(avl.height())

    x = np.arange(1, n + 1)
    y = np.array(heights)

    # Логарифмическая регрессия с основанием 2
    coeffs = np.polyfit(np.log2(x), y, 1)
    reg_curve = coeffs[0] * np.log2(x) + coeffs[1]

    print(f"Логарифмическая регрессия: h(n) = {coeffs[0]:.3f} * log2(n) + {coeffs[1]:.3f}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Фактическая высота")
    plt.plot(x, reg_curve, label="Регрессионная кривая", linestyle="--", color="orange")
    plt.xlabel("Количество ключей (n)")
    plt.ylabel("Высота дерева (h)")
    plt.title("Зависимость высоты AVL дерева от количества ключей")
    plt.legend()
    plt.grid(True)
    plt.show()

def generate_rbt_and_plot_with_regression(n):
    """Генерация красно-черного дерева и построение графика зависимости высоты от числа элементов"""
    heights = []
    rbt = RedBlackTree()

    for i in range(1, n + 1):
        rbt.insert(i)
        heights.append(rbt.height())

    x = np.arange(1, n + 1)
    y = np.array(heights)

    # Логарифмическая регрессия с основанием 2
    coeffs = np.polyfit(np.log2(x), y, 1)
    reg_curve = coeffs[0] * np.log2(x) + coeffs[1]

    print(f"Логарифмическая регрессия: h(n) = {coeffs[0]:.3f} * log2(n) + {coeffs[1]:.3f}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Фактическая высота")
    plt.plot(x, reg_curve, label="Регрессионная кривая", linestyle="--", color="orange")
    plt.xlabel("Количество ключей (n)")
    plt.ylabel("Высота дерева (h)")
    plt.title("Зависимость высоты красно-черного дерева от количества ключей")
    plt.legend()
    plt.grid(True)
    plt.show()

# Генерация данных и построение графика
# generate_bst_and_plot_with_regression(100)

Tree = AVLTree()
random_numbers = [random.randint(0, 100) for i in range(10)]  #генерация случайных чисел
for number in random_numbers:
    Tree.insert(number)

print("Последовательность входящих чисел: ", random_numbers)
print("Прямой обход (Pre-order):", Tree.preorder())
print("Симметричный обход (In-order):", Tree.inorder())
print("Обратный обход (Post-order):", Tree.postorder())
print("Обход в ширину (BFS):", Tree.bfs())
print("Отрисовка дерева:")
Tree.draw_tree()

print("Высота дерева: ", Tree.height())

# Поиск элемента
node = Tree.search(40)
if node is not None:
    print(f"Элемент {node.value} найден в дереве.")
else:
    print("Элемент не найден.")