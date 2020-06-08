#Integrative Practice 2
#By Manuel Ortiz Hernández-A01655515 and Mónica Lara Pineda-A01655306 at 2020
import re
from anytree import Node, RenderTree
def matching_string_to_proccess(index, char): 
    if string_to_process[index] == char:
        return True
    else: 
        return False

def left_most(production):
    i = 0
    if len(production) > len(string_to_process):
        return i
    while((i+1)!=len(production) and matching_string_to_proccess(i, production[i])):     
        i+=1
    return i

def parsing(new_production, dict_production,level,tree): 
    tree[new_production] = {}
    if string_to_process == new_production or level >= limit_of_tree:
        return tree
    index = left_most(new_production)
    non_t_symbol = new_production[index]
    if non_t_symbol in dict_production.keys(): 
        branch = 1
        for each_produc in dict_production[non_t_symbol]:
            production = new_production.replace(new_production[index], each_produc)
            tree[new_production][branch]= production
            branch+=1
            parsing(production, dict_production, level+1,tree)
    return tree

def print_tree(data, node):
    if node.name in data:
        for key in range(1, len(data[node.name])+1):
            temp = Node(data[node.name][key],parent=node)
            print_tree(data,temp)

def read_data():
    num = input("Enter the number of the file you want to read, 1-4: ")
    content = open("tests/test"+num+".txt", "r").readlines()
    lines = [line.strip() for line in content]
    non_terminal = lines[0].split(",")
    terminal = lines[1].split(",")
    start_symbol = lines[2]
    lines_produc = [line.replace("->", ",").split(",") for line in lines[3:]]
    grammar = {'Non-Terminal': non_terminal, 'Terminal': terminal,
               'Start_Symbol': start_symbol, 'Productions': {}}
    for n_t in non_terminal:
        grammar['Productions'][n_t] = []
    for each in lines_produc:
        if(each[0] in grammar['Productions']):
            grammar['Productions'][each[0]].append(each[1])
        else:
            grammar['Productions'][each[0]] = [each[1]]
    return grammar

def main():
    global string_to_process
    global limit_of_tree
    grammar = read_data()
    result = parsing(grammar['Start_Symbol'], grammar['Productions'], 0, tree = {})
    if string_to_process in result:
        print("I found a solution for this string.")
        root = grammar['Start_Symbol']
        tree = Node(root)
        print_tree(result,tree)
        for pre, fill, node in RenderTree(tree):
            print("%s%s" % (pre, node.name))
    else:
        print("Couldn't find a solution for this string.")

if __name__ == '__main__':
    string_to_process = input("Enter the string: ")
    limit_of_tree = int(input("Enter the level: "))
    main()