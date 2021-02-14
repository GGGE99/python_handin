import sys


def print_file_content(file):
    with open(file) as file_object:
        print(type(file_object))
        for line in file_object:
            print(line)


def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for t in lst:
            for element in t:
                file_object.write(str(element) + "\n")


def read_csv(input_file):
    li = []
    with open(input_file) as file_object:
        for line in file_object:
            li.append(line.split(","))
    return li


if __name__ == '__main__':
    args = sys.argv
    input = args[len(args)-1]
    lis = read_csv(input)

    if(args.__contains__("--help")):
        print("format = printer.py [options][file_to_read]")
        print("options:")
        print("    --file [location]to save output to a file")
    elif (args.__contains__("--file")):
        file = args[args.index("--file") + 1]
        write_list_to_file(file, lis)
    else:
        for l in lis:
            print(l)
