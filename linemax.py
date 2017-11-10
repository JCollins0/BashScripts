import sys as System
import os
import re

regex = re.compile(".*.out|.*.o")

def checkFile(fileName):
    F = open(fileName, 'r')
    i = 0
    for line in F:
        if(len(line) > 80):
            print(fileName + " "+ str(i+1) + " is longer than 80 characters.")
        i = i+1

if(len(System.argv) > 1):
    fileName = System.argv[1]
    if(os.path.isdir(fileName)):
        di = fileName
        files = os.listdir(di)
        for fi in files:
            fileName = di+"/"+fi
            if(not regex.match(fi)):
                checkFile(fileName)
    else:
        checkFile(fileName)
