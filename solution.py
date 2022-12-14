#IMPORTS
import time

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
        self.output = {target:""}
        self.searchAux(trie, target, l, r)
        return self.output
        
    def searchAux(self, trie, target, l, r):
        if l>r:
            return -1
    
        m = (l+r)//2
                
        lastChar = target[-1]
        if lastChar in trie and len(target)==1:         
            target = list(self.output.keys())[0]
            self.output[target]=trie[lastChar].ubication
            return self.output

        left = dict(list(trie.items())[m:r])         
        right = dict(list(trie.items())[l:m])
      
        if target[0] in right:
            left = self.searchAux(right[target[0]].children,target[1:],l,m)            
        elif target[0] in left:
            right = self.searchAux(left[target[0]].children,target[1:],m,r)
        else:
            return {}

#FUNCTIONS

def searchPattern(search, trie) : 
    if "and" in search:
        search = search.split(" and ")
        words = [search[0]]
        interception = trie.search(trie.root.children,search[0],0,len(trie.root.children.keys()))    
        for word in search[1:]:
            new = trie.search(trie.root.children,word,0,len(trie.root.children.keys()))
            words.append(word)
            equalFiles = set(interception[list(interception.keys())[0]].keys() & new[list(new.keys())[0]].keys())
            noEqualFiles = set(interception[list(interception.keys())[0]].keys() - new[list(new.keys())[0]].keys())
            newInterception = interception
            newInterception.update(new)        
            for key in newInterception.keys():
                for noEqual in noEqualFiles:
                    if noEqual in newInterception[key]:
                        del newInterception[key][noEqual]
            interception=newInterception  
        print("INTERCEPTION OF FILES: ",interception)
    elif "or" in search:
        search = search.split(" or ")
        union={}
        for word in search:
            dictionary = trie.search(trie.root.children,word,0,len(trie.root.children.keys()))
            union.update(dictionary)
        print("UNION OF FILES: ",union)
    else:
        dictionary = trie.search(trie.root.children,search,0,len(trie.root.children.keys()))
        print(dictionary)

def filesPrep(trie,fileNames) :
    for fileName in fileNames:
        file = open("archivos/"+fileName,"r", encoding="utf8")
        for i,line in enumerate(file):
            line = line.strip().split(" ")
            for word in line:
                trie.insert(word,fileName,i+1)
        file.close()


#CONSTANTS

fileNames = ["test01.txt","test02.txt","test03.txt"]
search = input("Ingrese el patron a buscar(and/or):")
# search = "colores and continentes and la"
# search = "colores or continentes or la"
start_time = time.time()
trie = Trie()                                         

#SEARCH PATTERN TESTS
filesPrep(trie,fileNames)
searchPattern(search,trie)

print("--- %s seconds ---" % (time.time() - start_time))
