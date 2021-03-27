# WIP

# playpen
Pull up a cookie-cutter file layout for a small project, get rid of it easily.

Playpen is designed to act like a scratchpad for programming ideas, pull up a preset project architecture, write a little bit of code to see how an idea works, and save it if you want to keep it.

## installing
* either unzip the code file into a directory you want to have this functionality in, or use git clone.
* run ```chmod +x problem.py```

## usage
`playpen make`
create new .playpen folder and set cwd.

`playpen make <template>`
creates new .playpen folder with a given file layout.

`-f`
copies file contents as well as layout from template.

`-g`
run git init in the playpen.


`playpen save <name>`
copy playpen from `./.playpen` into `./name` and remove .playpen.

`playpen template <name>`
add playpen to list of templates under a given name.


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

And adds a makefile with
```makefile
Main.class: Main.java
  javac Main.java
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

#### bash
Creates a main.sh file and inserts
```bash
#!/usr/bin/env bash
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
    "..."
    "<lang name n>": "files n"
  }
}
```

Where each group of files follows the syntax:
```json
[
  "<file 1>",
  "<file 2>",
  "...",
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
    "...,"
    "haskell": [
      {
        "filename": "main.hs",
        "contents": "main = putStrLn \"hello, world\""
      }
    ],
    "..."
  }
}
