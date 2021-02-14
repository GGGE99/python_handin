import os


def get_file_names(folderpath, out):
    arr = os.listdir()
    with open(out, 'w') as output:
        for n in arr:
            output.write(n + "\n")
    print(arr)
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""


def get_all_file_names(folderpath, out="none"):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    arr = []
    path = folderpath
    if(folderpath[-1] != "/"):
        path += '/'

    for root, dirs, files in os.walk(path):
        path = root.split(os.sep)
        #print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            print(len(path) * '---', file)
            arr.append(file)
    print(arr)
    with open(out, 'w') as output:
        for file in arr:
            output.write(file + '\n')


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file in file_names:
        with open(file) as f:
            print(f.readline() + file)


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


# print_line_one(["./test.txt","./tester.py","./testdir/secret.txt"])
# print_emails(["./test.txt", "./tester.py", "./testdir/secret.txt"])
write_headlines(["./test.txt", "./tester.py", "./testdir/secret.txt"], "./headlines.txt")