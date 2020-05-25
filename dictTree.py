from treelib import Node, Tree

#Cambiar key de parent por children o implementar las dos
dict_ = { "1": {'parent': None},"2": {'parent': "1"}, "3": {'parent': "2"}}

added = set()
tree = Tree()
while dict_:
    for key, value in dict_.items():
        if value['parent'] in added:
            tree.create_node(key, key, parent=value['parent'])
            added.add(key)
            dict_.pop(key)
            break
        elif value['parent'] is None:
            tree.create_node(key, key)
            added.add(key)
            dict_.pop(key)
            break

tree.show()
