#### Generate Metadata for all Traits
import json
import os
from FileWorker import layer_ranges

if not os.path.exists("./metadata"):
    os.makedirs("./metadata")

METADATA_FILE_NAME = "./metadata/all-traits.json"


def generate_metadata_all(all_images):

    for image in all_images:
        # replace indexes with modifiation itself and replace '-' to '_' in modifcation name
        for layer in layer_ranges:
            image[layer] = str(layer_ranges[layer][image[layer]]).replace("-","_")
            # if str(layer).find("-"):
            #     image[str(layer).replace("-","_")] = image.pop(layer)



    with open(METADATA_FILE_NAME, "w") as outfile:
        json.dump(all_images, outfile, indent=4)
