class TrieNode:
    def __init__(self, char):
        self.char = char            # guardamos el caracter en el nodo

        self.is_end = False         # preguntamos si es el final de la palabra

        self.counter = 0            # un contador que indica cuántas veces se inserta una palabra
                                    # (si el final de este nodo es Verdadero)

        self.children = {}          # un diccionario de nodos hijos
                                    # las claves son caracteres, los valores son nodos

class Trie(object):

    def __init__(self):
        self.root = TrieNode("")    # El trie tiene al menos el nodo raíz que no almacena ningún carácter.

    def insert(self, word):

        node = self.root            # Inserta una palabra en el trie

        # Recorre cada carácter de la palabra
        # Comprueba si hay algun hijo que contenga el carácter, y crea un nuevo hijo para el nodo actual
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # Si no se encuentra el caracter en los hijos, se crea un nuevo TrieNode
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True          # Marca el final de una palabra

        node.counter += 1           # Incrementar el contador para indicar que vemos esta palabra una vez más

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)


# t = Trie()
# t.insert("was")
# t.insert("word")
# t.insert("war")
# t.insert("what")
# t.insert("where")
# print(t.query("wh"))
# print(len(t.query("wh"))>0)


ubicaciones=[]
word = "wh"
archivo = open("archivo.txt","r")
for i,linea in enumerate(archivo):
    t = Trie()
    linea=linea.strip().split(" ")
    for palabra in linea:
        t.insert(palabra)
    if len(t.query(word))>0:
        ubicaciones.append(i)

print(ubicaciones)
