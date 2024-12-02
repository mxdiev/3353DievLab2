class AVLNode: #узел АВЛ-дерева
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1  # Высота узла


class AVLTree: #АВЛ-дерево
    
    def __init__(self):
        self.root = None

    def insert(self, key): #вызов операции вставки элемента
        self.root = self.insert2(self.root, key)

    def insert2(self, node, key): #рекурсивная вставка с балансировкой
        if node is None:
            return AVLNode(key)

        if key < node.value:
            node.left = self.insert2(node.left, key)
        else:
            node.right = self.insert2(node.right, key)

        #обновляем высоту
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        #балансировка
        balance = self.get_balance(node)
        
        #левый поворот
        if balance > 1 and key < node.left.value:
            return self.rotate_right(node)

        #правый поворот
        if balance < -1 and key > node.right.value:
            return self.rotate_left(node)

        #лево-правый поворот
        if balance > 1 and key > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        #право-левый поворот
        if balance < -1 and key < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

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
                stack.append(node.right)
                stack.append(node.left)
        return result

    def inorder(self): #симметричный обход
        result, stack, current = [], [], self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def postorder(self): #обратный обход
        stack, result = [(self.root, False)], []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.value)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result

    def bfs(self): #обход в ширину
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

    def get_height(self, node): #получить высоту узла
        return 0 if node is None else node.height

    def get_balance(self, node): #вычисление баланс-фактора
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z): #левый поворот вокруг узла z
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z): #правый поворот вокруг узла z
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def height(self): 
        if self.root is None:
            return 0
        return self.root.height