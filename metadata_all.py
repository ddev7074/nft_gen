#### Generate Metadata for all Traits
import json
import os

# os.mkdir(f"./metadata")

METADATA_FILE_NAME = "./metadata/all-traits.json"


def generate_metadata_all(all_images):
    with open(METADATA_FILE_NAME, "w") as outfile:
        json.dump(all_images, outfile, indent=4)
