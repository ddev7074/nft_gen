import os
from os import listdir
from os.path import isfile, join
import re
import json

layer_ranges = {}
layer_file_name = {}
conf = {}

def list_images(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles
def split_image_name(image_name):
    file_name = re.split('\\.', image_name)
    return re.split('_', str(file_name[0]).lower())

def fill_layer_ranges(files):
    layers = {}
    for file in files:
        layer_nr, layer_name, layer_modifier = split_image_name(file)
        uniq_layer_id = layer_name
        if uniq_layer_id in layers:
            layers[uniq_layer_id].append(layer_modifier)
        else:
            list_mod = []
            list_mod.append(layer_modifier)
            layers[uniq_layer_id] = list_mod
        if uniq_layer_id not in layer_file_name:
            layer_file_name[uniq_layer_id] = layer_nr + "_" + layer_name + "_"
    return layers

def validate_file_names(path):
    layer_name_nr = {}
    files = list_images(path)
    retval = True
    for file in files:
        if str(file).count('_') != 2:
            print(f"file {file} has invalid name!")
            retval = False
        else:
            layer_nr, layer_name, layer_modifier = split_image_name(file)
            if layer_name in layer_name_nr and layer_name_nr[layer_name] != layer_nr:
                print(f"wrong layer number for {layer_name} in file {file}")
                retval = False
            else:
                layer_name_nr[layer_name] = layer_nr
    return retval

def prepare_file_info(path):
    files = list_images(path)
    token_full_path = {}
    for file in files:
        token_id = re.split('\\.', file)
        full_path = os.path.abspath(file)
        token_full_path[token_id[0]] = str(full_path)
    return token_full_path

#load configuration
with open("./conf") as f:
    conf = json.load(f)


if not validate_file_names(conf["SRC_PATH"]):
    print("did not generate, there are files with invalid names")
    exit(1)
l_images = list_images(conf["SRC_PATH"])
layer_ranges = fill_layer_ranges(l_images)

# def main():
#     print("files in the directory")
#     l_images = list_images("./layers")
#     print(l_images)
#     layer_r = fill_layer_ranges(l_images)
#     print(layer_r)
# if __name__ == "__main__":
#     main()