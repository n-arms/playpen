# WIP

# playpen
Pull up a cookie-cutter file layout for a small project, get rid of it easily.

Playpen is designed to act like a scratchpad for programming ideas, pull up a preset project architecture, write a little bit of code to see how an idea works, and export it if you want to keep it.


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

