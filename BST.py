class BSTNode: #класс узла дерева
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST: #класс бинарного дерева поиска
    def __init__(self):
        self.root = None

    def insert(self, key): #вставка нового элемента
        if self.root is None:
            self.root = BSTNode(key)
            return
        current = self.root
        while True:
            if key < current.value:
                if current.left is None:
                    current.left = BSTNode(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(key)
                    return
                current = current.right

    def search(self, key): #поиск элемента
        current = self.root
        while current is not None:
            if key == current.value:
                return current
            elif key < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def preorder(self): #прямой обход
        stack, result = [self.root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)
                stack.append(node.right)  # Правое поддерево обрабатываем позже
                stack.append(node.left)  # Левое поддерево обрабатываем раньше
        return result

    def inorder(self): #симметричный обход
        result, stack, current = [], [], self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left  # Уходим влево
            current = stack.pop()
            result.append(current.value)  # Посещаем узел
            current = current.right  # Переходим направо
        return result

    def postorder(self): #обратный обход
        stack, result = [(self.root, False)], []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.value)  # Посещаем узел
                else:
                    stack.append((node, True))  # Помечаем как посещенный
                    stack.append((node.right, False))  # Обрабатываем правое поддерево
                    stack.append((node.left, False))  # Обрабатываем левое поддерево
        return result

    def bfs(self): #поиск в ширину
        result = []
        queue = []
        if self.root is not None:
            queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result
    
    def draw_tree(self): #вызов операции отрисовки дерева
        if self.root is None:
            print("Дерево пустое")
        else:
            self.draw_tree2(self.root, "", True)

    def draw_tree2(self, node, indent, is_last): #рекурсивная функция для отрисовки дерева
        if node is not None:
            #добавление линии для текущего узла
            print(f"{indent}{'└── ' if is_last else '├── '}{node.value}")

            #формируем префикс для дочерних узлов
            new_indent = indent + ("    " if is_last else "│   ")

            #рекурсивный вызов для правого и левого дочерних узлов
            if node.left:
                self.draw_tree2(node.left, new_indent, False)
            if node.right:
                self.draw_tree2(node.right, new_indent, True)
                
    def height(self): #вызов операции получения высоты дерева
        return self.get_height(self.root)
                
    def get_height(self, node): #рекурсивная функция получение высоты дерева
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, right_height)
