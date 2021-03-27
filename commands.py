import os, subprocess, queue

class CallStack:
    to_call = queue.Queue()

    @staticmethod
    def add(code):
        CallStack.to_call.put(code)

    @staticmethod
    def run():
        while not CallStack.to_call.empty():
            CallStack.to_call.get()()


def make_playpen(flags, args):

    if 'f' in flags:
        flags.remove('f')
        if len(args) == 0:
            print("not enough arguments, remove -f or add template name")
            return
        elif len(args) > 1:
            print("too many arguments, remove", args[1:])
            return
        else:
            os.mkdir('.playpen')

            if 'g' in flags:
                flags.remove('g')
                subprocess.call(['git', 'init'])


def save_playpen(flags, args):
    pass

def del_playpen(flags, args):
    pass

def template_playpen(flags, args):
    pass
