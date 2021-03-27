#!/usr/bin/env python3
import sys, commands

def parse_args():
    args = sys.argv[1:]
    print(args)
    flags = set()
    for i in range(len(args)-1, -1, -1):
        if args[i][0] == '-':
            flags.update([j for j in args[i][1:]])
            args.pop(i)
    return {"flags": flags, "mode": args[0], "args": args[1:]}

def main():
    args = parse_args()
    if args["mode"] == "make":
        commands.make_playpen(args["flags"], args["args"])
    elif args["mode"] == "save":
        commands.save_playpen(args["flags"], args["args"])
    elif args["mode"] == "del":
        commands.del_playpen(args["flags"], args["args"])
    elif args["mode"] == "template":
        commands.template_playpen(args["flags"], args["args"])
