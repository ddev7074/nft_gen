#### Generate Images
import os
from multiprocessing import Pool

from PIL import Image
from tqdm import tqdm

from generator import TOTAL_IMAGES
from gistfile import *

from FileWorker import layer_file_name, layer_ranges, conf

if not os.path.exists("./images"):
    os.makedirs("./images")

images_info = {}
layers_path = "layers"

def generate_images(all_images):
    for item in tqdm(all_images):
        generate_image(item)


def generate_image(item):
    width = conf["SIZE_W"]
    height = conf["SIZE_H"]
    image_properties = {}
    image_info = {}
    last_image = Image.new("RGBA", (width, height))
    for layer in layer_file_name:
        # if item[layer]: ??????
        image = Image.open(
            f"{layers_path}/{layer_file_name[layer]}{layer_ranges[layer][(item[layer])]}.png"
        ).convert("RGBA")
        image_properties[layer] = layer_ranges[layer][(item[layer])]
        last_image = Image.alpha_composite(last_image, image)

    rgb_im = last_image.convert("RGB")
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)


def generate_images_in_pool(all_images):
    with Pool(processes=conf["PROCESSES"]) as p:
        max_ = TOTAL_IMAGES
        with tqdm(total=max_) as pbar:
            for i, _ in enumerate(p.imap_unordered(generate_image, all_images)):
                pbar.update()
