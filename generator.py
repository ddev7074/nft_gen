import os
import random
from FileWorker import layer_ranges
from FileWorker import validate_file_names, conf

# TOTAL_IMAGES = os.environ.get("TOTAL_IMAGES", 10)
TOTAL_IMAGES = conf["TOTAL_IMAGES"]

all_images = []



def create_new_generic_image():
    new_image = {}

    for layer_name in layer_ranges:
        # gen random index of modification
        if len(layer_ranges[layer_name]) > 1:
            new_image[layer_name] = random.choices(range(0, len(layer_ranges[layer_name]) ))[0]
        else: # if there are no options, the index is always 0
            new_image[layer_name] = 0

    if new_image in all_images:
        return create_new_generic_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    # create_image_func, path = random.choices(
    #     [(create_new_image, "01"), (create_new_rare_image, "02")], [80, 20]
    # )[0]

    #create_image_func = create_new_image
    if not validate_file_names("./layers"):
        print("did not generate, there are files with invalid names")
        exit(1)
    create_image_func = create_new_generic_image
    path = "layers"
    new_trait_image = create_image_func()
    new_trait_image["path"] = path

    all_images.append(new_trait_image)
