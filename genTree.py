# python3 -m pip install treelib
from treelib import Node, Tree

#Primeros 3 niveles de test1.txt
tree = Tree()
tree.create_node("S", 0)  # root node
tree.create_node("AbB", 1, parent=0)
tree.create_node("bbS", 2, parent=0)
tree.create_node("bAbbB", 3, parent=1)
tree.create_node("abB", 4, parent=1)
tree.create_node("bbAbB", 5, parent=2)
tree.create_node("bbAbB", 6, parent=2)

tree.show()

# Productions dictionary
# {'S': ['AB'], 'A': ['aA', 'a'], 'B': ['BA', 'bbA', 'aS'], 'b': ['b']}}
