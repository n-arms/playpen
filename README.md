# prog-contest-tool
A bash script to help practice competitive programming. When practicing problems I find myself spending way too much time creating a new project folder, adding all the necessary files, writing a makefile, etc.

## installing
* either unzip the code file into a directory you want to have this functionality in, or use git clone.
* run ```chmod +x problem```

## usage
To run this code, simple use ```./problem problemname language```\
This will create a new folder called problemname, with files in it that are needed to develop a small, single file project in that language.

Additionally, it opens up the most relevant file in the default text editor.

## default support
By default, atom is the default text editor, and language support is proved for:

#### java
Creates a Main.java file and inserts:
```java
public class Main{
    public static void main(String[] args){

    }
}
```

#### python
Creates a main.py file and inserts
```python
print("hello, world!")
```

#### c++
Creates a main.cpp file and inserts
```cpp
#include <iostream>

int main(){
  return 0;
}
```

And adds a makefile with
```makefile
bin: main.cpp
  gcc -std=c++11 -Wall -Wextra -pedantic -O2 -o bin main.cpp
```

#### c
Creates a main.c file and inserts
```c
#include <stdio.h>

int main(){

}
```

And adds a makefile with
```makefile
bin: main.c
  cc -std=c99 -o bin main.c

```

## customization
Although a decent amount of functionality is provided out of the box, It is very easy to add new languages.

All customization should be done in config.json. It uses the following syntax:
```json
{
  "default-app": "<default text editor>",
  "languages": {
    "<lang name 1>": "files 1",
    "<lang name 2>": "files 2",
    ...
    "<lang name n>": "files n"
  }
}
```

Where each group of files follows the syntax:
```json
[
  "<file 1>",
  "<file 2>",
  ...
  "<file n>"
]
```

And each file:
```json
{
  "filename": "<name of file to be created>",
  "contents": "<contents of file to be created>"
}
```

For example, to add haskell support you might add the following to your config.json:

```json
{
  "default-app": "...",
  "languages": {
    ...,
    "haskell": [
      {
        "filename": "main.hs",
        "contents": "main = putStrLn \"hello, world\""
      }
    ],
    ...
  }
}
