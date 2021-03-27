#!/usr/bin/env python3
import os, sys, json, subprocess

def usage():
    print("usage: problem <problemname> <language>")

def open_file(name, lang, config):
    subprocess.run(["open", "-a", config["default-app"], name+"/"+config["languages"][lang][0]["filename"]])

def load_json():
    with open("config.json") as config_json_file:
        return json.load(config_json_file)

def parse_args(config):
    args = sys.argv[1:]
    flags = set()
    for i in range(len(args)-1, -1, -1):
        if args[i][0] == '-':
            flags.update([j for j in args[i][1:]])
            args.pop(i)
    print("args:", args)
    print("flags:", flags)
