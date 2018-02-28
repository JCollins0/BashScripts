# Useful bash/python scripts
script     |   dependencies | Usage
---------- | ---------------- | -----
[blocktext](/blocktext)  |  | ./blocktext "insert text here"
[checkhosts](/checkhosts) | [checkhosts.py](/checkhosts.py) | ./checkhosts
[chkprint](/chkprint) | | ./chkprint
[dirsize](/dirsize) | | ./dirsize 
[filelines](/filelines) | [filelines.py](/filelines.py) | ./filelines <file\>
[gitinit](/gitinit) | | ./gitinit -r <repository\>
[jumpto](/jumpto) | | . ./jumpto <directory_pattern\>
[listscripts](/listscripts) | | ./listscripts
[longlines](/longlines) | [longlines.py](/longlines.py) | ./longlines <directory\|file\> 
[note](/note) | | ./note \[-list\] \[-add <"Text"\>\] \[-clear\]
[proglog](/proglog) | | ./proglog -f <file\> -s <start time (24hr)\> -e <end time(24hr)\> -n <names.txt\> 
[rr](/rr) | | ./rr <num_players\> \[-auto\] \[-n <names.txt\>\]
[share](/share) | | ./share <abs. file path\> -u <user\>

If you want to use these scripts you should put them in a folder
and add the folder to your PATH by adding
```Bash
export PATH=file_path_to_folder/folder/:$PATH
```
to your .profile in home directory
