# albertauyeung.github.io/2020/06/15/python-trie.html/
# https://stackoverflow.com/questions/30910508/searching-a-string-inside-a-char-array-using-divide-and-conquer


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

        sorted(self.root.children.items(), key=lambda x: x[1].char, reverse=True)

    def divideYconquistaOutput(self, trie, objetivo, l, r):        
        self.output = {}
        self.divideYconquista(trie, objetivo, l, r)
        return self.output
        
    def divideYconquista(self, trie, objetivo, l, r):
        if l>r:                                         # return si l es mayor que r
            return -1
    
        m = (l+r)//2
        
        ultimoCaracter = objetivo[-1]
        if ultimoCaracter in trie and len(objetivo)==1:            
            self.output.update(trie[ultimoCaracter].ubicacion)
            return self.output
                        
        derecha = dict(list(trie.items())[l:m+1])         
        izquierda = dict(list(trie.items())[m-1:r])         
        
        if objetivo[0] in derecha:
            left = self.divideYconquista(derecha[objetivo[0]].children,objetivo[1:],l,len(derecha[objetivo[0]].children.keys()))            
        elif objetivo[0] in izquierda:
            right = self.divideYconquista(izquierda[objetivo[0]].children,objetivo[1:],m,r)
        else:
            return {}
        
nombArchivos = ["test01.txt","test02.txt","test03.txt"]
t = Trie()                                          #un trie para todos los archivos

# creacion del trie
for nombArchivo in nombArchivos:
    archivo = open("archivos/"+nombArchivo,"r", encoding="utf8")
    for i,linea in enumerate(archivo):
        linea = linea.strip().split(" ")
        for palabra in linea:
            t.insert(palabra,nombArchivo,i+1)
    archivo.close()

# busqueda
print(t.divideYconquistaOutput(t.root.children,"continente",0,len(t.root.children.keys())))
