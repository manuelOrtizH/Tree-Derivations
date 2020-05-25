  
import re
def matching_string_to_proccess(index, char): 
    if re.match(char, string_to_process[index]):
        return True
    else: 
        return False

def left_most(production, dict_produc):
    i = 0
    while((i+1)!=len(production) and matching_string_to_proccess(i, production[i])):     
        i+=1
    if production[i] in dict_produc.keys():
        return production[i]
    else:
        return False
    
def parsing(new_production, dict_production,level,tree): 
    if level >= limit_level:
        return tree
    if re.match(string_to_process, new_production):
        tree['String_Found'] = True 
        tree[new_production] = {}
        return tree
    non_t_symbol = left_most(new_production, dict_production)
    tree[new_production] = {}
    if non_t_symbol: 
        branch = 1
        for each_produc in dict_production[non_t_symbol]:
            production = re.sub(non_t_symbol, each_produc, new_production)
            tree[new_production][branch]= production
            branch+=1
            parsing(production, dict_production, level+1,tree)
    return tree

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
    global limit_level
    grammar = read_data()
    tree = {"String_Found": False}
    result = parsing(grammar['Start_Symbol'], grammar['Productions'], 0, tree)
    if result["String_Found"] == True:
        for each_node in result.items():
            print(each_node)
    else:
        print("Couldn't find a solution for this string. Miss you, Karen.")
    
if __name__ == '__main__':
    string_to_process = "aaa" 
    limit_level = 7
    main()