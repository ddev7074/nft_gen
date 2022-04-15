import json
import random

from IPython.display import display

from generator import all_images
from image_generator import generate_images_in_pool
from metadata import generate_metadata
from metadata_all import generate_metadata_all
from FileWorker import validate_file_names


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


def main():

    print("Are all images unique?", all_images_unique(all_images))
    # Add token Id to each image
    i = 0
    for item in all_images:
        item["tokenId"] = i
        i = i + 1

    generate_images_in_pool(all_images)
    generate_metadata_all(all_images)
    generate_metadata()


if __name__ == "__main__":
    main()
