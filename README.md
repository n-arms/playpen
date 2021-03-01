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
The following settings are in place by default:
* atom is the default text editor
* language support for:
  * java
    * creates a Main.java file
    * inserts:
    ```java
    public class Main{
        public static void main(String[] args){

        }
    }
    ```
  * python
    * creates a main.py file
    * inserts
    ```python
    print("hello, world!")
    ```

  * c++
    * creates a main.cpp file
    * inserts
    ```cpp
    #include <iostream>
    int main(){
      return 0;
    }
    ```

## customization
Although a decent amount of functionality is provided out of the box, It is very easy to add new languages.

All customization should be done in config.json. It uses the following syntax:
```json
{
  "default-app": "<default text editor>",
  "languages": {
    "<lang 1>": [
      "<file 1>",
      "<file 2>",
      ...
      "<file n>"
    ]
  }
}
```

Where each file follows the syntax:
```json
{
  "filename": "name of file to be created",
  "contents": "contents of file to be created"
}
```
