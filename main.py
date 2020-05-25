import re
def comparing_to_string(index, char): #Método para hacer la comparación entre un dos chars. Uno del string que se está procesando y el otro del string que se forma por la nueva production
    if string_to_process[index] == char:
        return True
    else: 
        return False

def find_non_terminal(production, dict_produc): #Método donde se busca un non-terminal símbolo. 
    i = 0
    while(True): #Loop para encontrar un non-terminal.
        if production[i] in dict_produc.keys(): #Se evalúa por char, si encuentra un non-terminal en el string
            #print("Found a symbol in position: {} in {} position".format(production[i], i))
            return production[i] #Regresa ese non-terminal
        if not comparing_to_string(i,production[i]): #En caso de que el char en evaluación no sea un non-terminal, se evalúa en otro método si el char en i se parece al char en i en el string que se está procesando
            return False 
            #Se regresa un Falso cuando hay una diferencia de chars en los dos strings. Ejemplo: String_to_process= "ba", production= "aa". Como el primer char es diferente, se corta la evaluación
            #Así se evita que se continúe desarrollando más ramas a partir de la production que entro en este método
        i+=1  

def parsing(new_production, dict_production, level, tree): #Método recursivo para formar el árbol y encontrar el string
    #print(new_production)
    if re.match(string_to_process, new_production): #Caso Base. Donde si la new_production es igual al string_to_process se muera todo
        return tree
    non_t_symbol = find_non_terminal(new_production, dict_production) 
    tree[level] = []
    if non_t_symbol != False: #Si se encontró un non-terminal símbolo 
        for each_produc in dict_production[non_t_symbol]: #Un loop en cada producción del non-terminal obtenido de la new_production
            #re.sub = sustituir cierto char con otro char o string 
            tree[level].append(re.sub(non_t_symbol, each_produc, new_production)) #Se agrega al diccionario resultante la nueva production
    for each in tree[level]: #Por cada nueva producción generada, entra a la recursividad, en donde each será el nuevo new_production de la otra llamada recursiva
        parsing(each, dict_production, level+1, tree) #Se agrega un nivel al tree
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
    # Creation of a dict inside of productions dict
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
    tree = {0: grammar['Start_Symbol']} #Utilizo este diccionario como un pseudo-árbol. Las llaves serán los nivels generados.
    result = parsing(grammar['Start_Symbol'], grammar['Productions'], 1, tree)
    print(result)


if __name__ == '__main__':
    string_to_process = "bAabaaa" 
    main()

