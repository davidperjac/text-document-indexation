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

    def dfs(self, node, prefix):                    #Depth-first traversal of the trie

        if node.is_end:                             #retornamos el diccionario con las ubicaciones

            # print("\n\nANTES DE AGREGAR                 ",self.output)
            # print("LO QUE TENGO QUE AGREGAR         ",node.ubicacion)

            for c,v in node.ubicacion.items():
                if c in self.output:
                    self.output[c]+=v
                else:
                    self.output[c]=v

            # print("YA AGREGADO                      ", self.output)

        for child in node.children.values():
            self.dfs(child, prefix + node.char)




    # Dada una entrada (un prefijo), recuperar todas las palabras almacenadas en el trie con ese prefijo
    def query(self, x):
        # Use a variable within the class to keep all possible outputs as there can be more than one word with such prefix
        self.output = {}
        node = self.root

        for char in x:                              # Check if the prefix is in the trie
            if char in node.children:
                node = node.children[char]
            else:
                return {}                           # cannot found the prefix, return empty list

        self.dfs(node, x[:-1])                      # Traverse the trie to get all candidates

        return self.output                          #retornamos la salida











    def  divideYconquista(self, objetivo, l, r):                    # l==0 && r==NMAX-1

        if l>r:                                         # return si l es mayor que r
            return -1

        m = (l+r)//2
        print("aaaaaa ",m)





        hijos = list(self.root.children.keys())




        # print(self.root.children.get("c"))
        # print(self.root.children.get("c").children.get("o"))






        print(hijos[l:m-1])
        # print(hijos[m+1:r])
        # print(objetivo)

        input()

        left = self.divideYconquista(objetivo, l, m - 1)  # replaced return

        # right = self.divideYconquista(objetivo, m+1, r)   #by saving values returned

        # if self==0:
        #     return m+1
        # elif l==r:                                      # returned -1 as the value has not matched and further recursion is of no use
        #     return -1
        # else:
        #     left = self.divideYconquista(self,l,m-1)    #replaced return
        #     right = self.divideYconquista(self,m+1,r)   #by saving values returned
        #     if left!=-1:                                #so that i can check them,
        #         return left                             #otherwise returning from here onlywould never allow second satatement to execute
        #     if right!=-1:
        #         return right
        #     else:
        #         return -1

        return 0


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
print(t.query("continente"))
