import re
def comparing_to_string(index, char): 
    if string_to_process[index] == char:
        return True
    else: 
        return False

def left_most(production, dict_produc):
    i = 0
    while(True):
        print("To check", production[i])
        if production[i] in dict_produc.keys():
            print("Found a symbol in position: {} in {} position".format(production[i], i))
            return production[i] 
        if not comparing_to_string(i,production[i]): 
            return False 
        i+=1  

def parsing(new_production, dict_production, tree): 
    #print(new_production)
    branch = 1 #Ahora, las keys serán las production y tendrán en ellas un diccionario con el número de ramas que contienen
    key_name = ",".join(new_production)
    if re.match(string_to_process, new_production): 
        return tree
    non_t_symbol = left_most(new_production, dict_production)
    tree[new_production] = {}
    if non_t_symbol != False: 
        for each_produc in dict_production[non_t_symbol]:
            production = re.sub(non_t_symbol, each_produc, new_production)
            tree[new_production][branch]= production
            branch+=1
            parsing(production, dict_production, tree)
    print(tree)
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
    grammar = read_data()
    print(grammar)
    result = parsing(grammar['Start_Symbol'], grammar['Productions'], tree={})
    print(result)



if __name__ == '__main__':
    string_to_process = "bbabaaa" 
    main()

