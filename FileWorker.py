from os import listdir
from os.path import isfile, join
import re

layer_ranges = {}
layer_file_name = {}

def list_images(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles
def split_image_name(image_name):
    file_name = re.split('\\.', image_name)
    return re.split('_', file_name[0])

def fill_layer_ranges(files):
    layers = {}
    for file in files:
        layer_nr, layer_name, layer_modifier = split_image_name(file)
        if layer_name in layers:
            layers[layer_name].append(layer_modifier)
        else:
            list_mod = []
            list_mod.append(layer_modifier)
            layers[layer_name] = list_mod
        if layer_name not in layer_file_name:
            layer_file_name[layer_name] = layer_nr + "_" + layer_name + "_"
    return layers

l_images = list_images("./layers")
layer_ranges = fill_layer_ranges(l_images)
# def main():
#     print("files in the directory")
#     l_images = list_images("./layers")
#     print(l_images)
#     layer_r = fill_layer_ranges(l_images)
#     print(layer_r)
# if __name__ == "__main__":
#     main()