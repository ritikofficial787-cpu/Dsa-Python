#Cration of Trie

class TrieNode:
    def __init__(self):
        self.children={}
        self.endofString=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

#Insert a string a Trie:-    
    def insertString(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node == None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endofString=True
        print("Successfullly Inserted")

#Search for a string in a Trie
# -Case1= String does not exist in trie
# -return: The String does not exist in Trie
# -Case2= String exists in Trie
#  -returm;- True
# -Case3= String is a prefix of another string, but it does not exist in a trie
# let we want to search in AP in API . so return:-False

    def searchString(self, word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node==None:
               return False
            currentNode=node
        if currentNode.endofString == True:
           return True
        else:
          return False
    
def deleteString(root, word, index):
    ch = word[index]
    currentNode=root.children.get(ch)
    canThisNodeBeDeleted=False

    if len(currentNode.children) >1:
        deleteString(currentNode, word, index+1)
        return False
    if index == len(word)-1:
       if len(currentNode.children)>=1:
           currentNode.endofString=False
           return False
       else:
           root.children.pop(ch)
           return True
    
    if  currentNode.endofString==True:
        deleteString(currentNode, word, index+1)
        return False
    
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted ==True:
        root.ch.pop(ch)
        return True
    
    
    else:
        return False








newTrie=Trie()
newTrie.insertString("RITIK")
newTrie.insertString("SINGH")
newTrie.insertString("SINGH")

deleteString(newTrie.root, "RITIK", 0)
print(newTrie.searchString("RITIK"))
print(newTrie.searchString("DCD"))
print(newTrie.searchString("RI"))

