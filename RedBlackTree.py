class RBNode: #узел красно черного дерева
    def __init__(self, key, color="red"):
        self.value = key
        self.color = color  #"red" или "black"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree: #красно-черное дерево
    def __init__(self):
        self.TNULL = RBNode(None, color="black")  #условный лист (черный, пустой)
        self.root = self.TNULL

    def insert(self, key): #вставка нового элемента с вызовом метода балансировки
        new_node = RBNode(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if key < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif key < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "red"
        self.balance_tree(new_node)

    def balance_tree(self, node): #балансировка после вставки
        while node != self.root and node.parent.color == "red":
            grandparent = node.parent.parent
            if node.parent == grandparent.left:
                uncle = grandparent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    grandparent.color = "red"
                    node = grandparent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = "black"
                    grandparent.color = "red"
                    self.rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    grandparent.color = "red"
                    node = grandparent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = "black"
                    grandparent.color = "red"
                    self.rotate_left(grandparent)

        self.root.color = "black"

    def search(self, key): #поиск элемента
        current = self.root
        while current != self.TNULL:
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
            if node != self.TNULL:
                result.append(node.value)
                stack.append(node.right)
                stack.append(node.left)
        return result

    def inorder(self): #симметричный обход
        result = []
        stack = []
        current = self.root

        while current is not None or stack:
            # Спускаемся до самого левого узла, добавляя узлы в стек
            while current is not None:
                stack.append(current)
                current = current.left
        
            # Берем узел из стека
            current = stack.pop()
        
            # Добавляем значение узла в результат
            result.append(current.value)
        
            # Переходим к правому поддереву
            current = current.right

        result = [x for x in result if x != None]
        return result

    def postorder(self): #обратный обход
        stack, result = [(self.root, False)], []
        while stack:
            node, visited = stack.pop()
            if node != self.TNULL:
                if visited:
                    result.append(node.value)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result
    
    def bfs(self): #обход в ширину
        result = []
        queue = [self.root] if self.root != self.TNULL else []
        while queue:
            node = queue.pop(0)
            if node != self.TNULL:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
        return result

    def draw_tree(self): #вызов операции отрисовки дерева
        if self.root is None:
            print("Дерево пустое")
        else:
            self.draw_tree2(self.root, "", True)

    def draw_tree2(self, node, indent, is_last): #рекурсивная функция для отрисовки дерева
        if node is not None:
            #определение цвета узла
            color = 'B' if node.color == 'black' else 'R'
            #добавление линии для текущего узла
            print(f"{indent}{'└── ' if is_last else '├── '}{node.value} ({color})")

            #формируем префикс для дочерних узлов
            new_indent = indent + ("    " if is_last else "│   ")

            #рекурсивный вызов для правого и левого дочерних узлов
            if node.left:
                self.draw_tree2(node.left, new_indent, False)
            if node.right:
                self.draw_tree2(node.right, new_indent, True)

    def rotate_left(self, node): #левый поворот
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.TNULL:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node): #правый поворот
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.TNULL:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child
    
    def height(self): #вызов операции получения высоты дерева
        return self.get_height(self.root)
                
    def get_height(self, node): #рекурсивная функция получение высоты дерева
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, right_height)
