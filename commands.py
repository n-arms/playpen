import os, subprocess, queue, shutil, sys, re

class CallQueue:
    def __init__(self, args):
        self.to_call = queue.Queue()
        self.args = args

    def add(self, code):
        self.to_call.put(code)

    def run(self):
        while not self.to_call.empty():
             self.args = self.to_call.get()(self.args)

def tree_walk(root):
    for dir in os.listdir(root):
        if os.path.isfile(os.path.join(os.getcwd(), dir)):
            print("file: ", dir)
        template_loader_wrapper([dir])

def make_playpen(flags, args):
    def git_wrapper(args):
        os.chdir('.playpen')
        subprocess.call(['git', 'init'])
        os.chdir('..')
        return args

    def playpen_init_wrapper(args):
        print("calling mkdir")
        os.mkdir(os.path.join(os.getcwd(), '.playpen'))
        return args

    def template_loader_wrapper(args):
        with open(os.path.join(os.getcwd(), sys.path[0], "templates.txt"), 'r') as templates:
            pattern = f'{args[0]}: ([^\\n]+)$'
            for line in templates:
                result = re.search(pattern, line)
                if result != None:
                    os.rmdir(os.path.join(os.getcwd(), '.playpen'))
                    shutil.copytree(result.group(1), os.path.join(os.getcwd(), ".playpen")) 
                    return args
        return args

    c = CallQueue(args)

    c.add(playpen_init_wrapper)
    if len(args) >= 1:
        c.add(template_loader_wrapper)

    if 'g' in flags:
        flags.remove('g')
        c.add(git_wrapper)

    if len(flags) > 0:
        print("illegal flags")
        return
    c.run()

def save_playpen(flags, args):
    def copy_wrapper(args):
        shutil.copytree(os.path.join(os.getcwd(), ".playpen"), os.path.join(os.getcwd(), args[0]))
        return args

    c = CallQueue(args)
    c.add(copy_wrapper)

    if len(flags) != 0 or len(args) != 1:
        print("illegal input")
        return
    c.run()
    return

def del_playpen(flags, args):
    def del_wrapper(args):
        shutil.rmtree(os.path.join(os.getcwd(), ".playpen"))
    c = CallQueue(args)
    c.add(del_wrapper)

    if len(flags) != 0 or len(args) != 0:
        print("illegal input")
        return
    c.run()
    return

def template_playpen(flags, args):
    def template_saver_wrapper(args):
        with open(os.path.join(os.getcwd(), sys.path[0], "templates.txt"), "a") as templates:
            templates.write(args[0]+": "+os.path.join(os.getcwd(), ".playpen")+"\n")

    c = CallQueue(args)
    c.add(template_saver_wrapper)

    if len(flags) != 0 or len(args) != 1:
        print('illegal input')
        return
    c.run()
    return
