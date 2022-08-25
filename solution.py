class TrieNode:
    def __init__(self, char):
        self.char = char            # guardamos el caracter en el nodo
        self.is_end = False         # ponemos que no es el final de la palabra
        self.children = {}          # tenemos un diccionario de nodos hijos donde las claves son caracteres y los valores son nodos
        self.ubicacion = {}         # tenemos un diccionario de ubicaciones donde las claves son archivos y los valores son las lineas

        
        
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode("")                    # El trie tiene al menos el nodo raíz que no almacena ningún carácter

    def insert(self, word, archivo, linea):
        node = self.root                            # Inserta una palabra en el trie

        for char in word:                           # Recorremos cada carácter de la palabra y comprueba si algun hijo contiene el carácter
            if char in node.children:
                node = node.children[char]
            else:                                   # Si no se encuentra el caracter en los hijos, se crea un nuevo TrieNode
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True                          # Marcamos el final de una palabra

        if archivo not in node.ubicacion:           # Agregamos la linea en la que se encuentra la palabra porque ya es el ultimo caracter
            node.ubicacion[archivo] = [linea]
        else:
            node.ubicacion[archivo].append(linea)

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:                             #retornamos el diccionario con las ubicaciones
            self.output.append((node.ubicacion))

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

        return self.output                      #retornamos la salida

    
    

nombArchivos = ["test01.txt","test02.txt","test03.txt"]
t = Trie()                                              #un trie para todos los archivos

# creacion del trie
for nombArchivo in nombArchivos:
    archivo = open("archivos/"+nombArchivo,"r", encoding="utf8")

    for i,linea in enumerate(archivo):
        linea = linea.strip().split(" ")
        for palabra in linea:
            t.insert(palabra,nombArchivo,i)
    archivo.close()

print(t.query("continentes"))
print(t.query("colores"))
