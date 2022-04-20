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
EXTERNAL_LINK = conf["EXTERNAL_LINK"]
SALE_TYPE = conf["SALE_TYPE"]
PRICE = conf["PRICE"]
METHOD = conf["METHOD"]
DURATION = conf["DURATION"]
SPECIFIC_BUYER = conf["SPECIFIC_BUYER"]
QUANTITY = conf["QUANTITY"]

def generate_metadata_all(all_images):
    token_path = prepare_file_info("./images")
    csv_data = []
    for image in all_images:
        csv_row = ""
        # image_properties = []
        image_properties = ""
        # replace indexes with modifiation itself and replace '-' to '_' in modifcation name
        for layer in layer_ranges:
            image[layer] = str(layer_ranges[layer][image[layer]]).replace("-"," ")
            if str(image[layer]).find("no ") != -1:
                image[layer] = "no"
            else:
                t = []
                t.append(layer)
                t.append(image[layer])
                if image_properties:
                    image_properties = image_properties + ", "
                image_properties = image_properties + json.dumps(t)
        tokenId = str(image["tokenId"])
        csv_row += token_path[tokenId] # file_path
        csv_row += ";;" # for double delimiter
        csv_row += f"{PROJECT_NAME} #{tokenId}" #nft_name
        csv_row += ";;" # for double delimiter
        csv_row += EXTERNAL_LINK #nft_name
        csv_row += ";;" # for double delimiter
        csv_row += PROJECT_DESC  # description
        csv_row += ";;" # for double delimiter
        csv_row += COLLECTION  # collection
        csv_row += ";;" # for double delimiter
        csv_row += image_properties  # properties
        csv_row += ";;" # for double delimiter
        csv_row += LEVELS  # levels
        csv_row += ";;" # for double delimiter
        csv_row += STATS  # stats
        csv_row += ";;" # for double delimiter
        csv_row += str(UNLOCKABLE_CONTENT )  # unlockable_content
        csv_row += ";;" # for double delimiter
        csv_row += str(EXPLICIT_AND_SENSITIVE_CONTENT)  # explicit_and_sensitive_content
        csv_row += ";;" # for double delimiter
        csv_row += str(SUPPLY)  # supply
        csv_row += ";;" # for double delimiter
        csv_row += BLOCKCHAIN  # blockchain
        csv_row += ";;" # for double delimiter
        csv_row += SALE_TYPE
        csv_row += ";;"  # for double delimiter
        csv_row += str(PRICE)
        csv_row += ";;"  # for double delimiter
        csv_row += json.dumps(METHOD)
        csv_row += ";;"  # for double delimiter
        csv_row += json.dumps(DURATION)
        csv_row += ";;"  # for double delimiter
        csv_row += json.dumps(SPECIFIC_BUYER)
        csv_row += ";;"  # for double delimiter
        csv_row += str(QUANTITY)
        csv_data.append(csv_row)

    with open(METADATA_FILE_NAME, "w") as outfile:
        json.dump(all_images, outfile, indent=4)

    csv_header = "file_path;;"
    csv_header += "nft_name;;"
    csv_header += "external_link;;"
    csv_header += "description;;"
    csv_header += "collection;;"
    csv_header += "properties;;"
    csv_header += "levels;;"
    csv_header += "stats;;"
    csv_header += "unlockable_content;;"
    csv_header += "explicit_and_sensitive_content;;"
    csv_header += "supply;;"
    csv_header += "blockchain;;"
    csv_header += "sale_type;;"
    csv_header += "price;;"
    csv_header += "method;;"
    csv_header += "duration;;"
    csv_header += "specific_buyer;;"
    csv_header += "quantity"

    with open(METADATA_CSV_FILE_NAME, 'w', newline = '') as csvfile:
        csvfile.write(csv_header)
        csvfile.write("\n")
        for row in csv_data:
            csvfile.write(row)
            csvfile.write("\n")