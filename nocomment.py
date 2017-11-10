import sys as System;

if(len(System.argv) > 1):
    #get file
    File = open(System.argv[1], 'r')
    FileOut = open("no_com_" + System.argv[1], 'w')
    output = ""
    foundMultiLine = False
    for line in File:
        Line = line.split("\r")[0].split("\n")[0]
        print(Line)
        foundMultiLineLine=1
        st = ""
        stlength = len(Line);
        for i in range(0, stlength):
            foundMultiLineLine = foundMultiLineLine + 1
            if(i+1 < stlength):
                if(Line[i] == '/' and Line[i+1] == '/'):
                    #single line: ignore rest of line
                    break
                elif(Line[i] == "/" and Line[i+1] == "*"): #multiline start
                    foundMultiLine = True
                elif(Line[i] == "*" and Line[i+1] == "/"): #multiline end
                    foundMultiLine = False
                    foundMultiLineLine=0
                else:
                    if( (not foundMultiLine) and foundMultiLineLine > 1):
                        st = st + Line[i];
            else: #last character in line
                if( (not foundMultiLine) and foundMultiLineLine > 1):
                    st = st + Line[i];
        if(not (st == '')):
            output = output + st + "\n"
    FileOut.write(output)
else:
    print("ERROR: Usage: python3 nocomment.py <file-name>")
