class TreeNode:
    def __init__(self,data,children=([])):
        self.data=data
        self.children=children

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret        
    
    def addchild(self, treenode):
        self.children.append(treenode)

tree=TreeNode('Drinks',[])
cold = TreeNode('Cold', [])
hot =TreeNode('Hot', [])
tree.addchild(hot)
tree.addchild(cold)
print(tree)
tea=TreeNode('Tea', [])
coffee=TreeNode('Coffee', [])
cola=TreeNode('COLA', [])
Mango=TreeNode('Mango', [])

cold.addchild(cola)
cold.addchild(Mango)

hot.addchild(tea)
hot.addchild(coffee)

print(tree)



