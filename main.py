def read_data():
    num = input("Enter the number of the file you want to read, 1-4: ")
    content = open("test"+num+".txt", "r").readlines()
    lines = [line.strip() for line in content]
    non_terminal = lines[0].split(",")
    terminal = lines[1].split(",")
    start_symbol = lines[2]
    lines_produc = [line.replace("->", ",").split(",") for line in lines[3:]]
    grammar = {'Non-Terminal': non_terminal, 'Terminal': terminal,
               'Start Symbol': start_symbol, 'Productions': {}}
    # Creation of a dict inside of productions dict
    for n_t in non_terminal:
        grammar['Productions'][n_t] = []
    for each in lines_produc:
        if(each[0] in grammar['Productions']):
            grammar['Productions'][each[0]].append(each[1])
        else:
            grammar['Productions'][each[0]] = [each[1]]
    print(grammar)
    print("moni, te amo")


def main():
    tree = read_data()


if __name__ == '__main__':
    main()
