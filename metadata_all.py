#### Generate Metadata for all Traits
import json
import os
import csv
from FileWorker import layer_ranges, prepare_file_info, conf
from  image_generator import  images_info

if not os.path.exists("./metadata"):
    os.makedirs("./metadata")

METADATA_FILE_NAME = "./metadata/all-traits.json"
METADATA_CSV_FILE_NAME = "./metadata/all-traits.csv"
PROJECT_NAME = conf["PROJECT_NAME"]
PROJECT_DESC = conf["PROJECT_DESC"]
COLLECTION = conf["COLLECTION"]
LEVELS = conf["LEVELS"]
STATS = conf["STATS"]
UNLOCKABLE_CONTENT = conf["UNLOCKABLE_CONTENT"]
EXPLICIT_AND_SENSITIVE_CONTENT = conf["EXPLICIT_AND_SENSITIVE_CONTENT"]
SUPPLY = conf["SUPPLY"]
BLOCKCHAIN = conf["BLOCKCHAIN"]


def generate_metadata_all(all_images):
    token_path = prepare_file_info("./images")
    csv_data = []
    for image in all_images:
        csv_row = []
        image_properties = []
        # replace indexes with modifiation itself and replace '-' to '_' in modifcation name
        for layer in layer_ranges:
            image[layer] = str(layer_ranges[layer][image[layer]]).replace("-"," ")
            if str(image[layer]).find("no ") != -1:
                image[layer] = "no"
            else:
                image_properties.append([layer,image[layer]])
        tokenId = str(image["tokenId"])
        csv_row.append(token_path[tokenId]) # file_path
        csv_row.append(f"{PROJECT_NAME} #{tokenId}") #nft_name
        csv_row.append(PROJECT_DESC)  # description
        csv_row.append(COLLECTION)  # collection
        csv_row.append(image_properties)  # properties
        csv_row.append(LEVELS)  # levels
        csv_row.append(STATS)  # stats
        csv_row.append(UNLOCKABLE_CONTENT)  # unlockable_content
        csv_row.append(EXPLICIT_AND_SENSITIVE_CONTENT)  # explicit_and_sensitive_content
        csv_row.append(SUPPLY)  # supply
        csv_row.append(BLOCKCHAIN)  # blockchain
        csv_data.append(csv_row)
    with open(METADATA_FILE_NAME, "w") as outfile:
        json.dump(all_images, outfile, indent=4)

    csv_header = ["file_path", "nft_name", "description", "collection", "properties", "levels", "stats", "unlockable_content", "explicit_and_sensitive_content", "supply", "blockchain"]
    with open(METADATA_CSV_FILE_NAME, 'w', newline = '') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ';')
        my_writer.writerow(csv_header)
        my_writer.writerows(csv_data)
