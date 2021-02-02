# prog-contest-tool
A bash script to help practice competitive programming. When practicing problems I find myself spending way too much time creating a new project folder, adding all the necessary files, writing a makefile, etc. 

## installing
* either unzip the code file into a directory you want to have this functionality in, or use git clone. 
* run ```chmod +x problem```

## usage
in its basic form you can call\
```./problem <foldername>```\
to create a new folder of a given name. To create a new folder and add the correct files to it, run:\
```./problem <foldername> -l <language>```\
by default the only languages are cpp, java and python. You can add more languages by adding them to the .problemconfig file. The file is then opened up using the text editor you specify in the .problemconfig (defaults to atom).

Additionally, creating a cpp file automatically adds and writes a makefile. This is hard coded into the scrpt and not part of the .problemconfig

## examples
```./problem traveling-sales-person -l cpp```\
create a folder called "traveling-sales-person", add and write a makefile, add the cpp file name in the .problemconfig, and write to it based off of the .problemconfig\
```./problem quicksort -l python```\
create a folder called "quicksort", add a file based off of the .problemconfig
