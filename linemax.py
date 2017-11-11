import sys as System
import os
import re

regex = re.compile("^\.") #filters folder and files that are hidden

def remove_hidden_files(array):
    narray = []
    for element in array:
        if(not regex.match(element)):
            narray.append(element)
    return narray

def is_binary(fileName):
    if(os.path.isdir(fileName)):
        return False
    finfo=os.popen('file -bi ' + "\""+fileName+ "\"",'r').read()
    charset = finfo.split(" ")[1].split("=")[1].strip()
    return charset == 'binary'

def checkFile(fileName):

    total_file_l_count = 0
    F = open(fileName, 'r')
    i = 0
    for line in F:
        if(len(line) > 80):
            print(fileName + " line", str(i+1))
            total_file_l_count = total_file_l_count +1
        i = i+1
    return total_file_l_count

def checkDirectory(directory):
    files_checked = 0
    total_file_l_count = 0
    files = os.listdir(directory)
    files = remove_hidden_files(files)
    for fi in files:
        fileName = directory+"/"+fi
        if(not is_binary(fileName) ):
            if(not os.path.isdir(fileName)):
                total_file_l_count = total_file_l_count + checkFile(fileName)
                files_checked = files_checked + 1
            else:
                (tfc, fc) = checkDirectory(fileName)
                total_file_l_count = total_file_l_count + tfc
                files_checked = files_checked + fc
    return (total_file_l_count, files_checked)

files_checked = 0
total_file_line_count = 0

if(len(System.argv) > 1):
    print()
    fileName = System.argv[1]
    if(os.path.isdir(fileName)):
        di = fileName
        (total_file_line_count, files_checked) = checkDirectory(di)
    else:
        total_file_line_count = checkFile(fileName)
        files_checked = 1
    print()
    print("checked",str(files_checked),
     "file(s). Found",str(total_file_line_count),"line(s) > 80.\n")
