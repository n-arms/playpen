import os, sys, json, subprocess

def usage():
    print("usage: problem <problemname> <language>")

def open_file(name, lang, config):
    subprocess.run(["open", "-a", config["default-app"], name+"/"+config["languages"][lang][0]["filename"]])

def load_json():
    with open("config.json") as config_json_file:
        return json.load(config_json_file)

def parse_args(config):
    for i in sys.argv:
        if i in config["languages"]:
            lang = i
        else:
            name = i
    return (lang, name)

def main():
    config = load_json()
    lang, name = parse_args(config)
    if (name is None or lang is None):
        usage()
        return

    os.mkdir(name)
    for file_pattern in config["languages"][lang]:
        with open(name+"/"+file_pattern["filename"], "w") as current_file:
            current_file.write(file_pattern["contents"])

    open_file(name, lang, config)

main()
