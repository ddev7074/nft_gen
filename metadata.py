import datetime
import json
import os

from metadata_model import AttributeModel, MetadataModel
from FileWorker import conf

# IMAGES_BASE_URL = os.environ.get("IMAGES_BASE_URL", "ipfs://<TOKEN>/")
IMAGES_BASE_URL = conf["IMAGES_BASE_URL"]
PROJECT_NAME = conf["PROJECT_NAME"]


def generate_metadata():
    timestamp = datetime.datetime.utcnow().timestamp()
    with open("./metadata/all-traits.json") as f:
        data = json.load(f)
        for row in data:
            token_id = row["tokenId"]
            token = MetadataModel(
                image=f"{IMAGES_BASE_URL}{token_id}.png",
                name=f"{PROJECT_NAME} #{token_id}",
                description=conf["PROJECT_DESC"],
                edition=token_id,
                date=int(timestamp),
                attributes=[
                    AttributeModel(trait_type=key, value=value)
                    for key, value in row.items()
                    if key != "path"
                ],
            )

            with open("./metadata/" + str(token_id), "w") as outfile:
                json.dump(token.dict(), outfile, indent=4)


if __name__ == "__main__":
    generate_metadata()
