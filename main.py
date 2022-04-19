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

def remove_dublicates(all_images):
    print("removing duplicates")
    uniq = list()
    for i in all_images:
        if not i in uniq:
            uniq.append(i)
    return uniq

def main():
    all_are_uniqe = all_images_unique(all_images)
    print("Are all images unique?", all_are_uniqe)
    uniq_images = list()
    if not all_are_uniqe:
        uniq_images = remove_dublicates(all_images)
        print(f"{len(all_images) - len(uniq_images)} images has been removed")
    else:
        uniq_images = all_images
    # Add token Id to each image
    i = 0
    for item in all_images:
        item["tokenId"] = i
        i = i + 1

    generate_images_in_pool(uniq_images)
    generate_metadata_all(uniq_images)
    generate_metadata()


if __name__ == "__main__":
    main()
