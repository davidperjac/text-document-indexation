# albertauyeung.github.io/2020/06/15/python-trie.html/
# https://stackoverflow.com/questions/30910508/searching-a-string-inside-a-char-array-using-divide-and-conquer


#CLASSES
class TrieNode:
    def __init__(self, char):
        self.char = char            # guardamos el caracter en el nodo
        self.is_end = False         # ponemos que no es el final de la palabra
        self.children = {}          # tenemos un diccionario de nodos hijos donde las claves son caracteres y los valores son nodos
        self.ubication = {}         # tenemos un diccionario de ubicaciones donde las claves son archivos y los valores son las lineas


class Trie(object):

    def __init__(self):
        self.root = TrieNode("")                    # El trie tiene al menos el nodo raíz que no almacena ningún carácter

    def insert(self, word, file, line):
        node = self.root                            # Inserta una palabra en el trie
        
        for char in word:                           # Recorremos cada carácter de la palabra y comprueba si algun hijo contiene el carácter
            if char in node.children:
                node = node.children[char]
            else:                                   # Si no se encuentra el caracter en los hijos, se crea un nuevo TrieNode
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True                          # Marcamos el final de una palabra

        if file not in node.ubication:              # Agregamos la linea en la que se encuentra la palabra porque ya es el ultimo caracter
            node.ubication[file] = set([line])
        else:
            node.ubication[file].add(line)

    def search(self, trie, target, l, r):        
        self.output = {}
        self.searchAux(trie, target, l, r)
        return self.output
        
    def searchAux(self, trie, target, l, r):
        if l>r:
            return -1
    
        m = (l+r)//2
                
        lastChar = target[-1]
        if lastChar in trie and len(target)==1:            
            self.output.update(trie[lastChar].ubication)
            return self.output

        left = dict(list(trie.items())[m:r])         
        right = dict(list(trie.items())[l:m])
      
        if target[0] in right:
            left = self.searchAux(right[target[0]].children,target[1:],l,m)            
        elif target[0] in left:
            right = self.searchAux(left[target[0]].children,target[1:],m,r)
        else:
            return {}


#TESTS

#TRIE PREPARATION
fileNames = ["test01.txt","test02.txt","test03.txt"]
trie = Trie()                                         

for fileName in fileNames:
    file = open("archivos/"+fileName,"r", encoding="utf8")
    for i,line in enumerate(file):
        line = line.strip().split(" ")
        for word in line:
            trie.insert(word,fileName,i+1)
    file.close()

#SEARCH TESTS
print("SEARCH TESTS")
print(trie.search(trie.root.children,"continentes",0,len(trie.root.children.keys())))
print(trie.search(trie.root.children,"colores",0,len(trie.root.children.keys())))
print(trie.search(trie.root.children,"la",0,len(trie.root.children.keys())))
print("")

#SEARCH
search = "colores and continentes and la"
# search = "colores or continentes or la"
if "and" in search:
    search = search.split(" and ")
    interception = trie.search(trie.root.children,search[0],0,len(trie.root.children.keys()))
    for word in search[1:]:
        new = trie.search(trie.root.children,word,0,len(trie.root.children.keys()))
        equalFiles = set(interception.keys())&set(new.keys())
        newInterception = {}
        for archivo in equalFiles:
            newInterception[archivo]=interception[archivo]|new[archivo]
        interception=newInterception
    print("INTERCEPTION OF FILES: ",interception)
elif "or" in search:
    search = search.split(" or ")
    union={}
    for word in search:
        dictionary = trie.search(trie.root.children,word,0,len(trie.root.children.keys()))
        for c,v in dictionary.items():
            if c not in union:
                union[c]=set(v)
            else:
                union[c]|=v        
    print("UNION OF FILES: ",union)
else:
    dictionary = trie.search(trie.root.children,search,0,len(trie.root.children.keys()))
    print(dictionary)
