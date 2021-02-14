import os
import sys

def get_file_names(folderpath, out):
    arr = os.listdir()
    with open(out, 'w') as output:
        for n in arr:
            output.write(n + "\n")
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""


def get_all_file_names(folderpath, out):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    arr = []
    path = folderpath
    if(folderpath[-1] != "/"):
        path += '/'

    for root, dirs, files in os.walk(path):
        path = root.split(os.sep)
        for file in files:
            arr.append(file)

    with open(out, 'w') as output:
        for file in arr:
            output.write(file + '\n')


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file in file_names:
        with open(file) as f:
            print(f.readline().rstrip("\n"))


def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file in file_names:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if line.__contains__("@"):
                    print(line.rstrip("\n"))

# @adadadasdasd


def write_headlines(md_files, out):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    linesarr = []
    for file in md_files:
        with open(file) as f:
            linesarr.append(f.readlines())
    with open (out, "w") as output:
        for lines in linesarr:
            for line in lines:
                if line.__contains__("#"):
                    print(line.rstrip("\n"))
                    output.write(line)


if __name__ == '__main__':
    args = sys.argv
    input = args[len(args)-1]

    if(args.__contains__("--help")):
        print("format = utils.py [options][files/dir_to_read]")
        print("options:")
        print("    -f [output_file] save name of all files in dir to output_file")
        print("    -fr [output_file] save name of all files in dir and its subdirs to output_file")
        print("    -l prints the first line of all files in the array")
        print("    -email prints all lines with an @ in the files")
        print("    -head [output_file] prints all lines with an # in the file")
    elif (args.__contains__("-f")):
        out = args[args.index("-f") + 1]
        get_file_names(input, out)
    elif (args.__contains__("-fr")):
        out = args[args.index("-fr") + 1]
        get_all_file_names(input, out)
    elif (args.__contains__("-l")):
        arr = []
        for i in range(args.index("-l") + 1, len(args)):
            arr.append(args[i])
        print_line_one(arr)
    elif (args.__contains__("-email")):
        arr = []
        for i in range(args.index("-l") + 1, len(args)):
            arr.append(args[i])
        print_emails(arr)
    elif (args.__contains__("-head")):
        out = args[args.index("-head") + 1]
        arr = []
        for i in range(args.index("-l") + 1, len(args)):
            arr.append(args[i])
        write_headlines(arr, out)
    else:
        for l in lis:
            print(l)