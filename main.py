import os, sys, json

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
    os.mkdir(name)
    for file_pattern in config["languages"][lang]:
        with open(name+"/"+file_pattern["filename"], "w") as current_file:
            current_file.write(file_pattern["contents"])

main()
