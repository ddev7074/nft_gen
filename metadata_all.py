#### Generate Metadata for all Traits
import json
import os

if not os.path.exists("./metadata"):
    os.makedirs("./metadata")

METADATA_FILE_NAME = "./all-traits.json"


def generate_metadata_all(all_images):
    with open(METADATA_FILE_NAME, "w") as outfile:
        json.dump(all_images, outfile, indent=4)
